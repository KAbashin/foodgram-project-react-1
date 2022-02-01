from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models


class CustomUser(AbstractUser):

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=254,
        unique=True
    )
    username = models.CharField(
        verbose_name='Уникальный юзернейм',
        max_length=150,
        unique=True,
        validators=[MinValueValidator(
            0, message='Переданное значение слишком короткое.'),
        ]
    )
    first_name = models.CharField(
        verbose_name='Имя', max_length=150)
    last_name = models.CharField(
        verbose_name='Фамилия', max_length=150)
    password = models.CharField(
        verbose_name='password', max_length=150)
    subscribe = models.ManyToManyField(
        verbose_name='Подписка',
        related_name='subscribers',
        to='self',
        symmetrical=False,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)
        constraints = (
            models.CheckConstraint(
                check=models.Q(username__length__gte=0),
                name='\nusername too short\n',
            ),
        )

    def __str__(self):
        return f'{self.username}: {self.email}'
