import pytest


class TestUsersAPI:
    url_create = '/api/users/'

    @pytest.mark.django_db(transaction=True)
    def test_users_not_authenticated(self, client):
        url = self.url_create
        response = client.get(url)

        code = 200
        assert response.status_code == code, (
            f'Анонимный пользователь при get запросе {url}'
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_users_authenticated(self, user_client):
        url = self.url_create
        response = user_client.get(url)

        code = 200
        assert response.status_code == code, (
            f'Авторизованный пользователь при get запросе {url}'
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_regisr_users_valid_data(self, client):
        url = self.url_create
        valid_data = {
            'email': 'vasya@yandex.ru',
            'username': 'vasya',
            'first_name': 'Вася',
            'last_name': 'Пупкин',
            'password': 'Qwerty123!'
        }
        response = client.post(url, data=valid_data)

        code = 201
        assert response.status_code == code, (
            f'При запросе с валидными данными на {url}'
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_regisr_users_not_valid_data(self, client):
        url = self.url_create
        not_valid_data = {
            'email': '11111111111',
            'username': '111111',
            'first_name': '111111',
            'last_name': '1111111',
            'password': 'Qwerty123!'
        }
        response = client.post(url, data=not_valid_data)

        code = 400
        assert response.status_code == code, (
            f'При запросе с не валидными данными на {url}'
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_regisr_users_invalid_data(self, client):
        url = self.url_create
        response = client.post(url, data=None)

        code = 400
        assert response.status_code == code, (
            f'При запросе без данных на {url}'
            f'должен получать ответ с кодом {code}'
        )

    # @pytest.mark.django_db(transaction=True)
    # def test_token_login(self, client):

    # Obtain a CSRF Token.
    #     response = client.post('/api/auth/token/login/')
    #     assert response.status_code == 201
    #     token = response.cookies['token']

    # Interact with the API.
    #     response = client.post('/api/auth/token/login/', json={
    #         'email': 'vasya@yandex.ru',
    #         'password': 'Qwerty123!'
    #     })
    #     token = response.COOKIES['auth_token']
    #
    #     assert token == True
