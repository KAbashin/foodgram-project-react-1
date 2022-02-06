import pytest


@pytest.fixture
def tag_1():
    from recipes.models import Tag
    return Tag.objects.create(name='Таг_1', color='#E26C2D', slug='Группа_1')

@pytest.fixture
def tag_2():
    from recipes.models import Tag
    return Tag.objects.create(name='Таг_2', color='#FF0000', slug='Группа_2')

@pytest.fixture
def ingredient_1():
    from recipes.models import Ingredient
    return Ingredient.objects.create(name='Ингредиент_1', measurement_unit='г.')

@pytest.fixture
def ingredient_2():
    from recipes.models import Ingredient
    return Ingredient.objects.create(name='Ингредиент_2', measurement_unit='г.')

@pytest.fixture
def recipe_1():
    from recipes.models import Recipe, Ingredient, Tag
    tag = Tag.objects.create(name='Таг_1', color='#E26C2D', slug='Группа_1')
    ingredient = Ingredient.objects.create(name='Ингредиент_2', measurement_unit='г.')
    return Recipe.objects.create(
            ingredients = [{'id': 1, 'amount': 10}],
            tags = [1],
            image = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAgMAAABieywaAAAACVBMVEUAAAD///9fX1/S0ecCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAACklEQVQImWNoAAAAggCByxOyYQAAAABJRU5ErkJggg==',
            name ='string',
            text = 'string',
            cooking_time = 1
    )

# @pytest.fixture
# def recope_2():
#     from recipes.models import Recipe
#     return Recipe.objects.create(
#         name='Ингредиент_2',
#         measurement_unit='г.'
#     )
