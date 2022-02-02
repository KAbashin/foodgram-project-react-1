import pytest


class TestFollowAPI:

    @pytest.mark.django_db(transaction=True)
    def test_subscriptions_not_authenticated(self, client):
        response = client.get('/api/users/subscriptions/')

        code = 401
        assert response.status_code == code, (
            'Анонимный пользователь при get запросе `/api/users/subscriptions/` '
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_subscriptions_authenticated(self, user_client):
        response = user_client.get('/api/users/subscriptions/')

        code = 200
        assert response.status_code == code, (
            'Авторизованный пользователь при get запросе `/api/users/subscriptions/` '
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_id_subscribe_not_authenticated(self, client, user_2):
        response = client.post(f'/api/users/{user_2.id}/subscribe/')

        code = 401
        assert response.status_code == code, (
            f'Анонимный пользователь при post запросе `/api/users/{user_2.id}/subscribe/` '
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_id_subscribe_authenticated(self, user_client, user_2):
        response = user_client.post(f'/api/users/{user_2.id}/subscribe/')

        code = 201
        assert response.status_code == code, (
            f'Авторизованный пользователь при post запросе "/api/users/"{user_2.id}"/subscribe/" '
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_id_subscribe_2_authenticated(self, user_1, user_2):
        response = user_1.post(f'/api/users/{user_2.id}/subscribe/')

        code = 201
        assert response.status_code == code, (
            f'Авторизованный пользователь при post запросе "/api/users/"{user_2.id}"/subscribe/" '
            f'должен получать ответ с кодом {code}'
        )
