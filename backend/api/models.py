from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()


class Tag(models.Model):
    "Тэги"
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
