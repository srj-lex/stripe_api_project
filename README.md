# stripe_api_project


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:srj-lex/stripe_api_project.git
```

Переименовать .env_example в .env, подставить свои значения.

Используя терминал и находясь в папке проекта выполнить команду:

```
docker build -t api_img:v1 .
```

Она соберет Docker-образ проекта.

После этого выполнить команду для запуска контейнера:

```
docker run --name api_container --rm -p 8000:8000 api_img:v1
```

Адрес расположения страницы товара:

```
http://localhost:8000/my_proj/item/1
```

Админка будет доступна по ссылке:

```
http://localhost:8000/admin
```