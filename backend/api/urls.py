from django.urls import include, path
from rest_framework import routers

from .views import TagViewSet, RecipeViewSet, IngredientViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'tags', TagViewSet, basename='tags')
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')


urlpatterns = [
    path('', include(router.urls)),
]
