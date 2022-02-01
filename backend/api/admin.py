from django.contrib.admin import register, ModelAdmin

from .models import Cart, Favorite, Ingredient, Recipe, Tag


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'color')


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = ('name', 'author')
    list_filter = ('author', 'name', 'tags')
    readonly_fields = ('count_favorites',)

    #TODO Добавить русское название строки
    def count_favorites(self, obj):
        return obj.favorites.count()


@register(Cart)
class CartAdmin(ModelAdmin):
    pass

@register(Favorite)
class FavoriteAdmin(ModelAdmin):
    pass
