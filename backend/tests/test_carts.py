# import pytest
#
# from api.models import Cart
#
#
# class TestCartAPI:
#
#     @pytest.mark.django_db(transaction=True)
#     def test_download_shopping_cart_not_authenticated(self, client):
#         response = client.get(f'/api/recipes/download_shopping_cart/')
#
#         code = 401
#         assert response.status_code == code, (
#             'Анонимный пользователь при get запросе `/api/recipes/download_shopping_cart/` '
#             f'должен получать ответ с кодом {code}'
#         )
#
#     @pytest.mark.django_db(transaction=True)
