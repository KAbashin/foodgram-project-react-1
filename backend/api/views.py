import io

from django.contrib.auth import get_user_model
from django.http import FileResponse, HttpResponse
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from django.db.models import Sum, F
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from recipes.models import Cart, Favorite, Ingredient, Recipe, Tag, \
    IngredientAmount
from users.models import Follow

from api.filters import TagFavoritShopingFilter
from api.permissions import AdminOrReadOnly, AdminUserOrReadOnly
from api.serializers import (FollowSerializer, IngredientSerializer,
                             RecipeSerializer, ShortRecipeSerializer,
                             TagSerializer)

User = get_user_model()


class TagsViewSet(ReadOnlyModelViewSet):
    permission_classes = (AdminOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientsViewSet(ReadOnlyModelViewSet):
    permission_classes = (AdminOrReadOnly,)
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        queryset = self.queryset
        if name:
            name = name.lower()
            start_queryset = list(queryset.filter(name__startswith=name))
            cont_queryset = queryset.filter(name__contains=name)
            start_queryset.extend(
                [i for i in cont_queryset if i not in start_queryset]
            )
            queryset = start_queryset
        return queryset


class FollowViewSet(UserViewSet):
    pagination_class = PageNumberPagination

    @action(
        methods=['post', ], detail=True, permission_classes=[IsAuthenticated])
    def subscribe(self, request, id=None):
        user = request.user
        author = get_object_or_404(User, id=id)

        if user == author:
            return Response({
                'errors': 'Ошибка подписки, нельзя подписываться на себя'
            }, status=status.HTTP_400_BAD_REQUEST)
        if Follow.objects.filter(user=user, author=author).exists():
            return Response({
                'errors': 'Ошибка подписки, вы уже подписаны на пользователя'
            }, status=status.HTTP_400_BAD_REQUEST)

        follow = Follow.objects.create(user=user, author=author)
        serializer = FollowSerializer(
            follow, context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @subscribe.mapping.delete
    def del_subscribe(self, request, id=None):
        user = request.user
        author = get_object_or_404(User, id=id)
        if user == author:
            return Response({
                'errors': 'Ошибка отписки, нельзя отписываться от самого себя'
            }, status=status.HTTP_400_BAD_REQUEST)
        follow = Follow.objects.filter(user=user, author=author)
        if follow.exists():
            follow.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({
            'errors': 'Ошибка отписки, вы уже отписались'
        }, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def subscriptions(self, request):
        user = request.user
        queryset = Follow.objects.filter(user=user)
        pages = self.paginate_queryset(queryset)
        serializer = FollowSerializer(
            pages,
            many=True,
            context={'request': request}
        )
        return self.get_paginated_response(serializer.data)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = PageNumberPagination
    filter_class = TagFavoritShopingFilter
    permission_classes = [AdminUserOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


    @action(detail=True, methods=['post', 'delete'],
            permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        if request.method == 'POST':
            return self.add_obj(Favorite, request.user, pk)
        elif request.method == 'DELETE':
            return self.delete_obj(Favorite, request.user, pk)
        return None

    @action(detail=True, methods=['post', 'delete'],
            permission_classes=[IsAuthenticated])
    def shopping_cart(self, request, pk=None):
        if request.method == 'POST':
            return self.add_obj(Cart, request.user, pk)
        elif request.method == 'DELETE':
            return self.delete_obj(Cart, request.user, pk)
        return None

    def add_obj(self, model, user, pk):
        if model.objects.filter(user=user, recipe__id=pk).exists():
            return Response({
                'errors': 'Ошибка добавления рецепта в список'
            }, status=status.HTTP_400_BAD_REQUEST)
        recipe = get_object_or_404(Recipe, id=pk)
        model.objects.create(user=user, recipe=recipe)
        serializer = ShortRecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_obj(self, model, user, pk):
        obj = model.objects.filter(user=user, recipe__id=pk)
        if obj.exists():
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({
            'errors': 'Ошибка удаления рецепта из списка'
        }, status=status.HTTP_400_BAD_REQUEST)


    #TODO Исправить
    @action(
        detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def download_shopping_cart(self, request):
        ingredients = IngredientAmount.objects.filter(
            recipe__cart__user=request.user).values(
            'ingredients__name',
            'ingredients__measurement_unit').annotate(total=Sum('amount'))
        shopping_list = 'список:\n'
        for ingredient in ingredients:
            shopping_list += (
                f'{ingredient["ingredients__name"]} '
                f'{ingredient["ingredients__measurement_unit"]}\n')

        purchase_list = 'foodgram_list.txt'
        response = HttpResponse(shopping_list, content_type='text/plain')
        response['Content-Disposition'] = (f'attachment;'
                                           f'filename={purchase_list}')
        return response