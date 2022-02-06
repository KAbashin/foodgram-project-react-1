import pytest

from recipes.models import Tag


class TestTagAPI:
    tags = '/api/tags/'

    @pytest.mark.django_db(transaction=True)
    def test_tag_not_authenticated(self, client):
        response = client.get(f'{self.tags}')

        code = 200
        assert response.status_code == code, (
            f'Анонимный пользователь при get запросе {self.tags} '
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_tag_authenticated(self, user_client):
        response = user_client.get(f'{self.tags}')

        code = 200
        assert response.status_code == code, (
            f'Авторизиванный пользователь при get запросе {self.tags} '
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_tag_id_not_authenticated(self, client, tag_1):
        response = client.get(f'{self.tags}{tag_1.id}/')

        code = 200
        assert response.status_code == code, (
            f'Анонимный пользователь при get запросе {self.tags}{tag_1.id}/'
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_tag_id_authenticated(self, user_client, tag_1):
        response = user_client.get(f'{self.tags}{tag_1.id}/')

        code = 200
        assert response.status_code == code, (
            f'Авторизованный пользователь при get запросе {self.tags}{tag_1.id}/'
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_tag_id_not_valid(self, client):
        response = client.get(f'{self.tags}4/')

        code = 404
        assert response.status_code == code, (
            f'Анонимный пользователь при get запросе {self.tags}4/ , '
            'на не существующий id'
            f'должен получать ответ с кодом {code}'
        )
