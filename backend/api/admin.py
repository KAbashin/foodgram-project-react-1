from django.contrib import admin

from .models import Recipe, Ingredient, Tag, Cart, Favorite, IngredientQuantity

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author',)
    list_filter = ('name', 'author', 'tags',)
    search_fields = ('name', 'author', 'tags',)
    empty_value_display = '-пусто-'


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    search_fields = ('name', 'measurement_unit',)
    list_filter = ('name',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag)
admin.site.register(Cart)
admin.site.register(Favorite)
admin.site.register(IngredientQuantity)
