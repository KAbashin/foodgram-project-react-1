from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()


class Tag(models.Model):
    RED = '#FF0000'
    GREEN = '#008000'
    ORANGE = '#FFA500'
    YELLOW = '#FFFF00'
    BLUE = '#0000FF'
    BROWN = '#A52A2A'
    FUCHSIA = '#FF00FF'

    COLOR_CHOICES = [
        (RED, 'Желтый'),
        (GREEN, 'Зеленый'),
        (ORANGE, 'Оранжевый'),
        (YELLOW, 'Желтый'),
        (BLUE, 'Синий'),
        (BROWN, 'Коричневый'),
        (FUCHSIA, 'Фиолетовый')
    ]

    name = models.CharField(verbose_name='Тэг', max_length=150, unique=True)
    color = models.CharField(max_length=7, unique=True, choices=COLOR_CHOICES,verbose_name='Цвет')
    slug = models.SlugField(verbose_name='Slug тэга', max_length=150, unique=True)

    class Meta:
        ordering = ['id', ]
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


    def __str__(self):
        return self.slug


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название ингредиента', max_length=200, unique=True)
    measurement_unit = models.CharField(
        verbose_name='Единица измерения', max_length=20)


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='recipes',
                               verbose_name='Автор рецепта')
    name = models.CharField(verbose_name='Название рецепта', max_length=200)
    image = models.ImageField(verbose_name='Изображение рецепта',
                              upload_to='recipes/')
    text = models.TextField(verbose_name='Описание рецепта')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientQuantity',
        verbose_name='Ингредиенты',
        related_name='recipes'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Тэги',
        help_text='Установите тэг'
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления',
        validators=[MinValueValidator(
            1, message='Минимальное время приготовления 1 минута'),]
    )
