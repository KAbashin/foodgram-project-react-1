from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Тэг', max_length=150, unique=True)
    color = models.CharField(
        verbose_name='Цветовой HEX-код', max_length=7,
        unique=True, default='FF'
    )
    slug = models.CharField(
        verbose_name='Слаг тэга', max_length=150, unique=True)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['-id']

    def __str__(self) -> str:
        return f'{self.name}'


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название ингредиента', max_length=200)
    measurement_unit = models.CharField(
        verbose_name='Единицы измерения', max_length=20)

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        ordering = ['-name']
        constraints = [
            models.UniqueConstraint(fields=['name', 'measurement_unit'],
                                    name='unique_ingredient')
            ]

    def __str__(self) -> str:
        return f'{self.name}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор рецепта',
        related_name='recipes',
    )
    name = models.CharField(
        verbose_name='Название рецепта', max_length=200)
    image = models.ImageField(
        verbose_name='Изображение рецепта', upload_to='recipe_images/')
    text = models.TextField(
        verbose_name='Описание рецепта')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='recipes.AmountIngredient',
        verbose_name='Ингредиенты',
        related_name='recipes'
    )
    tags = models.ManyToManyField(
        Tag, verbose_name='Тег', related_name='recipes')
    favorite = models.ManyToManyField(
        verbose_name='Избранные рецепты',
        related_name='favorites',
        to=User,
    )
    cart = models.ManyToManyField(
        verbose_name='Список покупок',
        related_name='carts',
        to=User,
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления',
        validators=[MinValueValidator(
            1, message='Минимальное время приготовления 1 минута'),
        ]
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('pub_date', )
        constraints = (
            models.UniqueConstraint(
                fields=('name', 'author'),
                name='unique_for_author'
            ),
        )

    def __str__(self) -> str:
        return f'{self.name}'


class AmountIngredient(models.Model):
    ingredients = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Связанные ингредиенты',
        related_name='recipe',

    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='В каких рецептах',
        related_name='ingredient',

    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        validators=[MinValueValidator(
            1, message='Минимальное количество ингредиентов 1'),
        ]
    )

    class Meta:
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингридиентов'
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(fields=['ingredient', 'recipe'],
                                    name='unique ingredients recipe')
        ]

    def __str__(self) -> str:
        return f'{self.amount} {self.ingredients}'
