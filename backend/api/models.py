from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

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

    name = models.CharField(
        verbose_name='Тэг', max_length=150, unique=True)
    color = models.CharField(
        verbose_name='Цвет', max_length=7, choices=COLOR_CHOICES, unique=True)
    slug = models.SlugField(
        verbose_name='Slug тэга', max_length=150, unique=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.slug


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название ингредиента', max_length=200)
    measurement_unit = models.CharField(
        verbose_name='Единица измерения', max_length=20)

    class Meta:
        ordering = ['-name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        constraints = [
            models.UniqueConstraint(fields=['name', 'measurement_unit'],
                                    name='unique ingredient')
        ]

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта'
    )
    name = models.CharField(
        verbose_name='Название рецепта', max_length=200)
    image = models.ImageField(
        verbose_name='Изображение рецепта', upload_to='recipes/')
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
            1, message='Минимальное время приготовления 1 минута'),
        ]
    )
    pub_date = models.DateField(
        verbose_name='Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['pub_date']
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Рецепт'
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Корзина'
        verbose_name_plural = 'В корзине'
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique cart user')
        ]


class IngredientQuantity(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE,
        verbose_name='Ингредиент'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )
    quantity = models.PositiveSmallIntegerField(
        verbose_name='Количество', validators=[MinValueValidator(
            1, message='Минимальное количество ингредиентов 1'),
        ]
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'
        constraints = [
            models.UniqueConstraint(fields=['ingredient', 'recipe'],
                                    name='unique ingredients recipe')
        ]


class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт'
    )

    class Mets:
        ordering = ['-id']
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'],
                                    name='unique favorite recipe for user')
        ]
