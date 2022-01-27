from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.models import Tag, Recipe, Cart, Favorite, Ingredient

User = get_user_model()


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class RecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class IngredientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
