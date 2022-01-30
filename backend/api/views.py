from rest_framework import viewsets
from .models import Tag, Recipe, Cart, Favorite, Ingredient
from .serializers import (TagSerializers, RecipeSerializers, CartSerializers,
                          FavoriteSerializers, IngredientSerializers)
from .permissions import UserOrReadOnly, AuthorOrReadOnly


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    permission_classes = (UserOrReadOnly,)

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers
    permission_classes = (UserOrReadOnly,)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializers
