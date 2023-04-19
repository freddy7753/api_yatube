# api_yatube
# API Yatube
## Данный проект представляет собой RESTful API для приложения Yatube.

# Аутентификация

## Аутентификация осуществляется по токену TokenAuthentication. Для получения токена нужно отправить POST-запрос на auth/token/login/ с параметрами username и password. В ответ на запрос будет получен токен, который нужно передавать в заголовке Authorization.

# Примеры использования API
>- Получение списка всех постов

``` GET /api/v1/posts/ ```

>- Создание нового поста

``` POST /api/v1/posts/ ```

>- Обновление поста

``` PUT /api/v1/posts/<post_id>/ ```

>- Удаление поста

``` DELETE /api/v1/posts/<post_id>/ ```

>- Получение списка всех комментариев к посту

``` GET /api/v1/posts/<post_id>/comments/ ```


