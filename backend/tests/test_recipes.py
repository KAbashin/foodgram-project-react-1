# import pytest
#
# from api.models import Recipe
#
#
# class TestRecipeAPI:
#
#     @pytest.mark.django_db(transaction=True)
#     def test_recipe_not_authenticated(self, client):
#         response = client.get(f'/api/recipes/')
#
#         code = 200
#         assert response.status_code == code, (
#             'Анонимный пользователь при get запросе `/api/recipes/` '
#             f'должен получать ответ с кодом {code}'
#         )
#
#     @pytest.mark.django_db(transaction=True)
#     def test_create_recipe_not_authenticated(self, client):
#         response = client.post(f'/api/recipes/')
#
#         code = 401
#         assert response.status_code == code, (
#             'Анонимный пользователь при post запросе `/api/recipes/` '
#             f'должен получать ответ с кодом {code}'
#         )
#
#     @pytest.mark.django_db(transaction=True)
#     def test_recipe_authenticated(self, user_client):
#         response = user_client.get(f'/api/recipes/')
#
#         code = 200
#         assert response.status_code == code, (
#             'Авторизованный пользователь при get запросе `/api/recipes/` '
#             f'должен получать ответ с кодом {code}'
#         )
#
#     @pytest.mark.django_db(transaction=True)
#     def test_create_recipe_authenticated(self, user_client):
#         response = user_client.get(f'/api/recipes/')
#
#         code = 200
#         assert response.status_code == code, (
#             'Авторизованный пользователь при post запросе `/api/recipes/` '
#             f'должен получать ответ с кодом {code}'
#         )