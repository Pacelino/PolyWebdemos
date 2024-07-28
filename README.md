> Версия Python 3.12.4

### Виртуальное окружение
Когда откроете на своем компьютере, создайте виртуальное окружение в папке проекта 
1. Установка виртуального окружения.
```
python3.12 -m venv venv
```
Потом появляется папка venv в проекте.

2. Дальше активируем окружение
для mac os или linux
```
source ./venv/bin/activate
```
или для windows
```
.\venv\Scripts\activate
```
Если все прошло удачно, то появляется (venv) вначале строки.

Библиотеки, которые на данный момент установил хранятся в файле requirements.txt
1) запускаете виртуальное окружение (писал выше как сделать)
2)  вначале командной строки должно быть (venv) 
3) пишете
```
pip install -r requirements.txt
```
чтобы установить все библиотеки в свое окружение.

### Установка пароля от бд и секретных ключей
Создайте в папке PolyWebdemos файл `local_settings.py` и вставте в него такой шаблон. Замените значение словаря под свои.
 В переменной DATABASES хранятся параметры подключения к базе.
```python
from .settings import *
import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'имя_базы_данных',
        'USER': 'имя_пользователя_базы_данных',
        'PASSWORD': 'пароль_от_базы_данных',
        'HOST': 'хост (Например: localhost)',
        'PORT': 'порт_от_базы_данных (по умолчанию 5432)',
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-gq)^&u)sn#&8@@t$51*67&6&qq5z)67m^$rdz9ljf48%nc$uld'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
```
### Подключение PostgreSQL

Устанавливаете себе [PostgreSql](https://www.postgresql.org/). Посмотрите пункт *Установка пароля от бд и секретных ключей*.
После подключения проведите миграции:
```
python manage.py migrate
```
или для linux, mac os 
```
./manage.py migrate
```
Если подключение прошло успешно, миграции будут созданы без ошибок.
### Тестовый запуск проекта
Для запуска сервера используйте одну из следующих команд:
```
python manage.py runserver --settings=PolyWebdemos.local_settings
```
или для linux, mac os 
```
./manage.py runserver --settings=PolyWebdemos.local_settings
```
Если на экране появилась начальная страница, значит, все работает правильно!
