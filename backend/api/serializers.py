from numpy import source
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Tag, Recipe, Cart, Favorite, Ingredient
from users.models import Follow
from users.serializers import CustomUserSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='author.email')
    id = serializers.ReadOnlyField(source='author.id')
    username = serializers.ReadOnlyField(source='author.username')
    first_name = serializers.ReadOnlyField(source='author.first_name')
    last_name = serializers.ReadOnlyField(source='author.last_name')
    is_subscribed = serializers.SerializerMethodField()
    recipes = serializers.SerializerMethodField()
    recipes_count = serializers.SerializerMethodField()

    class Meta:
        model = Follow
        fields = ('email', 'id', 'username', 'first_name', 'last_name', 
                  'is_subscribed', 'recipes_count')

    def get_is_subscribed(self, object):
        return Follow.objects.filter(
            user=object.user, author=object.author
        ).exists()

    def get_recipes(self, object):
        return Recipe.objects.filter(author=object.author)

    def get_recipes_count(self, object):
        return Recipe.objects.filter(author=object.author).count()
