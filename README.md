> Версия Python 3.12.4

### Виртуальное окружение
Когда откроете на своем компьютере, создайте виртуальное окружение в папке проекта 
1. Установка виртуального окружения.
```
python3.12 -m venv venv
```
Потом появляется папка venv в проекте.
2. Дальше активируем окружение
mac os или linux
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

### Подключение PostgreSQL
Устанавливаете себе на PostgreSql  (https://www.postgresql.org/)

Создайте в ней базу с названием "webdemos_bd"
В django проекте в файле settings.py есть переменная DATABASES. В ней хранятся параметры подключения к базе (по вашему усмотрению можете все поменять). 
Напишите в ней своего пользователя (по дефолту postgres) и свой пароль, который написали при скачивании postgreSQL.
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
python manage.py runserver
```
или для linux, mac os 
```
./manage.py runserver
```
Если на экране появилась начальная страница, значит, все работает правильно!