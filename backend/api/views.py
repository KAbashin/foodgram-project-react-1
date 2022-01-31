from rest_framework import viewsets
from .models import Tag, Recipe, Cart, Favorite, Ingredient
from .serializers import TagSerializer, RecipeSerializer, IngredientSerializer
from .permissions import UserOrReadOnly, AuthorOrReadOnly


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (UserOrReadOnly,)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (UserOrReadOnly,)


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
