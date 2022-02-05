import pytest


# @pytest.fixture
# def tag_1():
#     from api.models import Recipe
#     return Recipe.objects.create(name='Таг_1', color='RED', slug='Группа_1')


@pytest.fixture
def tag_1():
    from recipes.models import Tag
    return Tag.objects.create(name='Таг_1', color='BLUE', slug='Группа_1')


@pytest.fixture
def ingredient_1():
    from recipes.models import Ingredient
    return Ingredient.objects.create(name='Ингредиент_1', measurement_unit='г.')
