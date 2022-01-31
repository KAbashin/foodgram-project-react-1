# import pytest
#
# from users.models import Follow
#
#
# class TestFollowAPI:
#
#     @pytest.mark.django_db(transaction=True)
#     def test_subscriptions_not_authenticated(self, client):
#         response = client.get('/api/users/subscriptions/')
#
#         code = 401
#         assert response.status_code == code, (
#             'Анонимный пользователь при get запросе `/api/users/subscriptions/` '
#             f'должен получать ответ с кодом {code}'
#         )