# Сайт с рецептами
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)
[![Django-app workflow](https://github.com/romangrbr/foodgram-project-react/actions/workflows/main.yml/badge.svg)]

## Описание:

«Продуктовый помощник»
На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, 
добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, 
необходимых для приготовления одного или нескольких выбранных блюд.


### Pytest
В проекте есть тесты основного функционала и эндпоинтов которые можно запустить командой pytest

### Admin
Do not change the name and password data ))

- Username: foodgramadmin
- Password: foodgramadmin

### Основные адреса: 

| Адрес                 | Описание |
|:----------------------|:---------|
| adminca.ml            | Главная страница |
| adminca.ml/admin/     | Для входа в панель администратора |
| adminca.ml/api/docs/  | Описание работы API |

## Пользовательские роли
| Функционал                                                                                                                | Неавторизованные пользователи |  Авторизованные пользователи | Администратор  |
|:--------------------------------------------------------------------------------------------------------------------------|:---------:|:---------:|:---------:|
| Доступна главная страница.                                                                                                | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна и работает форма авторизации                                                                                     | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна страница отдельного рецепта.                                                                                     | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна и работает форма регистрации.                                                                                    | :heavy_check_mark: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна страница «Мои подписки»                                                                                          | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Можно подписаться и отписаться на странице рецепта                                                                        | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Можно подписаться и отписаться на странице автора                                                                         | :x: | :heavy_check_mark: | :heavy_check_mark: |
| При подписке рецепты автора добавляются на страницу «Мои подписки» и удаляются оттуда при отказе от подписки.             | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна страница «Избранное»                                                                                             | :x: | :heavy_check_mark: | :heavy_check_mark: |
| На странице рецепта есть возможность добавить рецепт в список избранного и удалить его оттуда                             | :x: | :heavy_check_mark: | :heavy_check_mark: |
| На любой странице со списком рецептов есть возможность добавить рецепт в список избранного и удалить его оттуда           | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна страница «Список покупок»                                                                                        | :x: | :heavy_check_mark: | :heavy_check_mark: |
| На странице рецепта есть возможность добавить рецепт в список покупок и удалить его оттуда                                | :x: | :heavy_check_mark: | :heavy_check_mark: |
| На любой странице со списком рецептов есть возможность добавить рецепт в список покупок и удалить его оттуда              | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Есть возможность выгрузить файл (.txt) с перечнем и количеством необходимых ингредиентов для рецептов из «Списка покупок» | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Ингредиенты в выгружаемом списке не повторяются, корректно подсчитывается общее количество для каждого ингредиента        | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна страница «Создать рецепт»                                                                                        | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Есть возможность опубликовать свой рецепт                                                                                 | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Есть возможность отредактировать и сохранить изменения в своём рецепте                                                    | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Есть возможность удалить свой рецепт                                                                                      | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна и работает форма изменения пароля                                                                                | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна возможность выйти из системы (разлогиниться)                                                                     | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Доступна и работает система восстановления пароля.                                                                        | :x: | :heavy_check_mark: | :heavy_check_mark: |
| Изменять пароль любого пользователя.                                                                                      | :x: | :x: | :heavy_check_mark: |
| Создавать/блокировать/удалять аккаунты пользователей.                                                                     | :x: | :x: | :heavy_check_mark: |
| Редактировать/удалять любые рецепты.                                                                                      | :x: | :x: | :heavy_check_mark: |
| Добавлять/удалять/редактировать ингредиенты.                                                                              | :x: | :x: | :heavy_check_mark: |
| Добавлять/удалять/редактировать теги.                                                                                     | :x: | :x: | :heavy_check_mark: |



## Администратор и админ-зона
:one: Все модели выведены в админ-зону с возможностью редактирования и удаление записей.  
:two: Для модели пользователей включена фильтрация списка по имени и email.  
:three: Для модели рецептов включена фильтрация по автору, названию рецепта, тегам.  
:four: На админ-странице рецепта отображается общее число добавлений этого рецепта в избранное.  
:five: Для модели ингредиентов включена фильтрация по названию.  

## Создание пользователя администратором
Пользователя может создать администратор — через админ-зону сайта или через POST-запрос на специальный эндпоинт api/users/ (описание полей 
запроса для этого случая — в документации).  Далее пользователь отправляет POST-запрос с параметрами email и password на эндпоинт /api/auth/token/, 
в ответе на запрос ему приходит token, как и при самостоятельной регистрации.

## Запуск проекта

- Клонировать репозиторий GitHub (не забываем создать виртуальное окружение и установить зависимости):
[https://github.com/RomanGrbr/foodgram-project-react.git](https://github.com/RomanGrbr/foodgram-project-react.git)

- Создать файл .env в папке проекта:
```
EMAIL_HOST_USER=user@yandex.ru
EMAIL_HOST_PASSWORD=wer123
SECRET_KEY=p&l%385148kl9(vs
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
ALLOWED_HOSTS='*'
```

- в Docker cоздаем образ :

```
docker build -t foodgram .
```
- Собираем контейнеры:
```
docker-compose up -d
```
- В результате должны быть собрано три контейнера, при введении следующей команды получаем список запущенных контейнеров:  
```
docker-compose ps
```  
_Пример:_  

```
CONTAINER ID   IMAGE                             COMMAND                  CREATED       STATUS       PORTS                               NAMES
ffbe984f7533   nginx:1.19.3                      "/docker-entrypoint.…"   3 weeks ago   Up 3 weeks   0.0.0.0:80->80/tcp, :::80->80/tcp   romangrbr_nginx_1
5166bcfb1188   romangrbr/mysite:latest           "/bin/sh -c 'gunicor…"   3 weeks ago   Up 3 weeks                                       romangrbr_backend_1
a9c7a7542ddb   postgres:12.4                     "docker-entrypoint.s…"   3 weeks ago   Up 3 weeks   5432/tcp                            romangrbr_db_1
```
Назначение контейнеров:  

|          IMAGES           | NAMES                |        DESCRIPTIONS         |
|:-------------------------:|:---------------------|:---------------------------:|
|       nginx:1.19.3        | romangrbr_nginx_1    |   контейнер HTTP-сервера    |
|       postgres:12.4       | romangrbr_db_1       |    контейнер базы данных    |
| romangrbr/backend:latest  | romangrbr_backend_1  | контейнер приложения Django |
| romangrbr/frontend:latest | romangrbr_frontend_1 | контейнер приложения React  |


- Сделать миграции, создать суперпользователя и собрать статику:
```
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input 
docker-compose exec backend python manage.py loaddata db.json
```

- Для переноса данных с файла ingredients.json на PostgreSQL выполним несколько команд:
    ```
    docker-compose exec backend python manage.py shell 
    ```
    ```
    >>> exec(open("/backend/static/data/filldb.py").read())
    ```
    ```
    docker-compose exec backend
    ```

### Автор проекта:
_Гербер Роман_  
**email:** _romangrbr@gmail.com_  
**telegram:** _@romangrbr_  
