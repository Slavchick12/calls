#  Calls - сервис автоматических звонков
![example workflow](https://github.com/Slavchick12/calls/actions/workflows/main.yml/badge.svg)
## Описание проекта
Сервис предназначен для взаимодействия с рецептами. У пользователей есть возможность создавать рецепты, изменять их, добавлять в избранное, а также подписываться на других авторов. Раздел «Список покупок» позволит пользователям составить список ингредиентов и их количество для приготовления выбранных блюд, который можно скачать в формате «.txt».
## Описание Workflow
###### tests
- Проверка кода на соответствие PEP8.
## Функционал
#### Весь функционал осуществляется авторизованными пользователями
* Пользователь может задать параметры подключения к поставщику телефонии: адрес sip шлюза, имя пользователя, пароль и т.п. (только одну запись)
* Пользователь может загружать звуковые файлы
* Пользователь может загружать .txt файлы со списком телефонных номеров
* Инициировать дозвон до базы абонентов с воспроизведением загруженного звукового файла
## Права доступа
###### Неавторизованный пользователь
* Создание пользователя
* Получение JWT-токена пользователя
###### Авторизованный пользователь
* Изменить имя своего аккаунта
* Изменить пароль своего аккаунта
* Удалить свой аккаунт
* Получить звуковой файл
* Получить список своих загруженных звуковых файлов
* Загрузить звуковой файл
* Удалить звуковой файл
* Получить параметры подключения
* Создать параметры подключения
* Изменить параметры подключения
* Удалить параметры подключения
* Получить базу абонентов
* Получить список баз абонентов
* Загрузить базу абонентов
* Удалить базу абонентов
## Подготовка и запуск проекта
#### Клонирование репозитория
###### Склонируйте репозиторий на локальную машину:
```bash
git clone git clone https://github.com/Slavchick12/calls.git
```
#### Подготовка базы данных PostgreSQL
###### Шаг 1. Скачайте и установите PostreSQL 14.5
```
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
```
###### Шаг 2. Запустите PostgreSQL и создайте БД "hotel"
#### Настройка виртуального окружения и проведение миграций
###### Шаг 1. Установка виртуального окружения
```bash
cd <path_to_project/>
```
```bash
python -m venv venv
```
###### Шаг 2. Активация виртуального окружения
```bash
. venv/Scripts/activate
```
###### Шаг 3. Обновление пакетов pip
```bash
python -m pip install -U pip
```
###### Шаг 4. Установка зависимостей проекта
```bash
pip install -r requirements.txt
```
###### Шаг 5. Перейдите в директорию с файлом manage.py с запущенным виртуальным окружением
```bash
cd <path_to_project>/calls/
```
###### Шаг 6. Проведение миграций
```bash
python manage.py makemigrations
python manage.py migrate
```
#### Подготовка секретных переменных
###### Шаг 1. Перейдите в корень проекта
```bash
cd <path_to_project>/
```
###### Шаг 2. Создайте файл *.env* на примере файла *.env.example*

#### Запуск проекта на локальной машине
```bash
cd <path_to_project>/calls/
```
```bash
python manage.py runserver
```
#### Создание суперюзера
```bash
python manage.py createsuperuser
```
#### Админ-панель Django
```bash
http://<host>/admin
```
#### Swagger
```bash
http://<host>/swagger
```
## Стек технологий
[![Python](https://img.shields.io/badge/-Python-16a5f7?logo=Python)](https://www.python.org/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-0b4711?logo=Django)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-0b75b3?logo=PostgreSQL)](https://www.postgresql.org/)
[![Swagger](https://img.shields.io/badge/-Swagger-15b02f?logo=Swagger)](https://swagger.io/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-94c1eb?logo=GitHub%20actions)](https://github.com/features/actions)
#### Development tools
[![Flake8](https://img.shields.io/badge/-flake8-ced126)](https://flake8.pycqa.org/)
[![Wemake-python-styleguide](https://img.shields.io/badge/-wemake%20python%20styleguide-ced126)](https://pypi.org/project/wemake-python-styleguide/)
[![Isort](https://img.shields.io/badge/-isort-ced126)](https://pypi.org/project/isort/)
[![Black](https://img.shields.io/badge/-black-ced126)](https://pypi.org/project/black/)
