import pytest


class TestIngredientAPI:
    url_ingr = '/api/ingredients/'

    @pytest.mark.django_db(transaction=True)
    def test_ingredient_not_authenticated(self, client):
        response = client.get(f'{self.url_ingr}')

        code = 200
        assert response.status_code == code, (
            f'Анонимный пользователь при get запросе {self.url_ingr}'
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_ingredient_authenticated(self, user_client):
        response = user_client.get(f'{self.url_ingr}')

        code = 200
        assert response.status_code == code, (
            f'Авторизованный пользователь при get запросе `{self.url_ingr}` '
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_ingredient_id_authenticated(self, user_client, ingredient_1):
        response = user_client.get(f'{self.url_ingr}{ingredient_1.id}/')

        code = 200
        assert response.status_code == code, (
            f'Авторизованный пользователь при get запросе '
            f'- на {self.url_ingr}{ingredient_1.id}/'
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_ingredient_id_not_authenticated(self, client, ingredient_1):
        response = client.get(f'{self.url_ingr}{ingredient_1.id}/')

        code = 200
        assert response.status_code == code, (
            f'Анонимный пользователь при get запросе '
            f'- на {self.url_ingr}{ingredient_1.id}/'
            f'должен получать ответ с кодом {code}'
        )
