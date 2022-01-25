from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Recipe(models.Model):
    "Рецепты"
    pass

class Teg(models.Model):
    "Тэги"
    name = models.CharField('Имя тэга', max_length=256)
    # color = models.CharField()
    slug = models.SlugField('Slug тэга', max_length=150, unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['id', ]

class Ingredient(models.Model):
    "Ингредиенты"
    pass
