import pytest
from rest_framework.test import APIClient


@pytest.fixture
def user_1(django_user_model):
    user = django_user_model.objects.create_user(
            email='lesha@yandex.ru',
            username='lesha',
            first_name='Леша',
            last_name='Патрон',
            password='Qwerty123!'
        )
    client = APIClient()
    client.force_authenticate(user=user)
    return client

# @pytest.fixture
# def user_1():
#     client = APIClient()
#     client.force_authenticate(user=None)
#     return client


@pytest.fixture
def user_2(django_user_model):
    return django_user_model.objects.create_user(
            email='petya@yandex.ru',
            username='petya',
            first_name='Петя',
            last_name='Васичкин',
            password='Qwerty123!'
        )


@pytest.fixture
def another_user(django_user_model):
    return django_user_model.objects.create_user(username='TestUserAnother', password='1234567')


# @pytest.fixture
# def token(user):
#     from rest_framework.authtoken.models import Token
#     refresh = Token.key(user)

#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }


@pytest.fixture
def user_client(django_user_model):
    user = django_user_model.objects.create_user(
        email= 'vasya@yandex.ru',
        username= 'vasya',
        first_name = 'Вася',
        last_name = 'Пупкин',
        password = 'Qwerty123!'
    )
    client = APIClient()
    client.force_authenticate(user=user)
    return client
