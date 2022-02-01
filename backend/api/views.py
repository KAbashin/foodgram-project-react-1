
from rest_framework import status, viewsets

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from api.models import (Cart, Favorite, Ingredient, IngredientQuantity, Recipe,
                        Tag)
from api.permissions import IsAdminOrReadOnly
from api.serializers import ( IngredientSerializer,
                             RecipeSerializer, TagSerializer)


class TagsViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('name')


class IngredientsViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer



class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    pagination_class = LimitOffsetPagination
