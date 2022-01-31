import pytest


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(username='TestUser', password='1234567')


@pytest.fixture
def user_2(django_user_model):
    return django_user_model.objects.create_user(username='TestUser2', password='1234567')


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
    from rest_framework.test import APIClient
    # user = django_user_model.objects.create_user(username='TestUser', password='1234567')
    client = APIClient()
    client.force_authenticate(user=None)
    return client
