import pytest


class TestRecipeAPI:
    url_recipe = '/api/recipes/'

    @pytest.mark.django_db(transaction=True)
    def test_recipe_not_authenticated(self, client):
        response = client.get(f'{self.url_recipe}')

        code = 200
        assert response.status_code == code, (
            f'Анонимный пользователь при get запросе {self.url_recipe}'
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_create_recipe_not_authenticated(self, client):
        response = client.post(f'{self.url_recipe}')

        code = 401
        assert response.status_code == code, (
            f'Анонимный пользователь при post запросе {self.url_recipe}'
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_recipe_authenticated(self, user_client):
        response = user_client.get(f'{self.url_recipe}')

        code = 200
        assert response.status_code == code, (
            f'Авторизованный пользователь при get запросе {self.url_recipe}'
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_create_recipe_authenticated(self, user_client):
        response = user_client.get(f'{self.url_recipe}')

        code = 200
        assert response.status_code == code, (
            f'Авторизованный пользователь при post запросе {self.url_recipe}'
            f'должен получать ответ с кодом {code}'
        )
