from django.http import HttpResponse, FileResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from rest_framework import status, viewsets
from rest_framework.status import HTTP_400_BAD_REQUEST
import io
from rest_framework.viewsets import ReadOnlyModelViewSet
from api.filters import TagFilter
from recipes.models import (
    Cart, Favorite, Ingredient, IngredientAmount, Recipe, Tag)
from api.permissions import AdminOrReadOnly, AdminUserOrReadOnly
from api.serializers import (ShortRecipeSerializer, IngredientSerializer,
                             RecipeSerializer, TagSerializer)
from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination
from api.serializers import FollowSerializer
from users.models import Follow

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

    @action(methods=['post',], detail=True, permission_classes=[IsAuthenticated])
    def subscribe(self, request, id=None):
        '''Подписаться'''
        user = request.user
        author = get_object_or_404(User, id=id)

        if user == author:
            return Response({
                'errors': 'Ошибка подписки, нельзя подписываться на самого себя'
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
    filter_class = TagFilter
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

    #TODO Уточнить
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def download_shopping_cart(self, request):
        user = get_object_or_404(User, username=request.user.username)
        shopping_cart = user.cart.all()
        dict = {}
        for num in shopping_cart:
            ingredients_list = num.recipe.recipe_ingredient.all()
            for ingredient in ingredients_list:
                name = ingredient.ingredient.name
                amount = ingredient.amount
                measurement_unit = ingredient.ingredient.measurement_unit
                if name not in dict:
                    dict[name] = {
                        'measurement_unit': measurement_unit,
                        'amount': amount}
                else:
                    dict[name]['amount'] += amount
        list = []
        i = 0
        for key in dict:
            i += 1
            list.append(f'{i}. {key} - {dict[key]["amount"]} - '
                        f'{dict[key]["measurement_unit"]}')
        buffer = io.BytesIO()
        pdfmetrics.registerFont(TTFont('TNRB', 'timesbd.ttf'))
        p = canvas.Canvas(buffer)
        p.setFont('TNRB', 16)
        x = 0
        for int in range(len(list)):
            x = x + 20
            p.drawString(20, 727 - x, list[int])
        p.showPage()
        p.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='canvas.pdf')