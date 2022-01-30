import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


class TestJWT:
    # url_login = 'api/auth/token/login/'
    url_create = '/api/users/'
    # url_refresh = '/api/v1/jwt/refresh/'
    # url_verify = '/api/v1/jwt/verify/'

    @pytest.mark.django_db(transaction=True)
    def test_jwt_create__invalid_request_data(self, client, user):
        url = self.url_create
        response = client.post(url)
        code_expected = 401
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` неавторизованным пользователем, '
            f'возвращается код {code_expected}'
        )
        fields_invalid = ['username', 'password']
        for field in fields_invalid:
            assert field in response.json().keys(), (
                f'Убедитесь, что при запросе `{url}` без параметров, '
                f'возвращается код {code_expected} с сообщением о том, '
                'при обработке каких полей возникла ошибка.'
                f'Не найдено поле {field}'
            )

        username_invalid = 'invalid_username_not_exists'
        password_invalid = 'invalid pwd'
        data_invalid = {
            'username': username_invalid,
            'password': password_invalid
        }
        response = client.post(url, data=data_invalid)
        code_expected = 401
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        field = 'detail'
        assert field in response.json(), (
            f'Убедитесь, что при запросе `{url}` с некорректным username, '
            f'возвращается код {code_expected} с соответствующим сообщением '
            f'в поле {field}'
        )
        username_valid = user.username
        data_invalid = {
            'username': username_valid,
            'password': password_invalid
        }
        response = client.post(url, data=data_invalid)
        assert response.status_code == code_expected, (
            f'Убедитесь, что при запросе `{url}` без параметров, '
            f'возвращается код {code_expected}'
        )
        field = 'detail'
        assert field in response.json(), (
            f'Убедитесь, что при запросе `{url}` с некорректным password, '
            f'возвращается код {code_expected} с соответствующим сообщением '
            f'в поле {field}'
        )
