import pytest

from api.models import Tag


class TestTagAPI:

    @pytest.mark.django_db(transaction=True)
    def test_tag_not_authenticated(self, client):
        response = client.get(f'/api/tags/')

        code = 200
        assert response.status_code == code, (
            'Анонимный пользователь при get запросе `/api/tags/` '
            f'должен получать ответ с кодом {code}'
        )

    @pytest.mark.django_db(transaction=True)
    def test_tag_id_not_authenticated(self, client, tag_1):
        response = client.get(f'/api/tags/{tag_1.id}')

        code = 200
        assert response.status_code == code, (
            'Анонимный пользователь при get запросе `/api/tags/id` '
            f'должен получать ответ с кодом {code}'
        )