from django.urls import include, path
from rest_framework import routers

from .views import (TagViewSet, RecipeViewSet, CartViewSet,
                    FavoriteViewSet, IngredientViewSet)

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'tags', TagViewSet, basename='tags')
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'recipes/download_shopping_cart', CartViewSet, basename='cart')
router.register(
    r'recipes/(?P<title_id>\d+)/shopping_cart', CartViewSet, basename='shopping_cart')
router.register(
    r'recipes/(?P<title_id>\d+)/favorite', FavoriteViewSet, basename='favorite')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')


urlpatterns = [
    path('', include(router.urls)),
]
