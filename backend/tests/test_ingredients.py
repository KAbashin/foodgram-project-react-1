import pytest

from api.models import Ingredient


class TestRecipeAPI:

    @pytest.mark.django_db(transaction=True)
    def test_ingredient_not_authenticated(self, client):
        response = client.get(f'/api/ingredients/')

        code = 401
        assert response.status_code == code, (
            'Анонимный пользователь при get запросе `/api/ingredients/` '
            f'должен получать ответ с кодом {code}'
        )
    
    @pytest.mark.django_db(transaction=True)
    def test_ingredient_authenticated(self, user_client):
        response = user_client.get(f'/api/ingredients/')

        code = 200
        assert response.status_code == code, (
            'Авторизованный пользователь при get запросе `/api/ingredients/` '
            f'должен получать ответ с кодом {code}'
        )
    
    @pytest.mark.django_db(transaction=True)
    def test_ingredient_authenticated(self, user_client, ingredient_1):
        response = user_client.get(f'/api/ingredients/{ingredient_1.id}')

        code = 200
        assert response.status_code == code, (
            'Авторизованный пользователь при get запросе `/api/ingredients/id` '
            f'должен получать ответ с кодом {code}'
        )
