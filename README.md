# Poil au Nez Web Application  *Django*
**This is a website like a blog with an interface admin to manage it. It's a [Django](https://www.djangoproject.com) Web application for the company of clown theater 'Poil au Nez'.
So, to install and use it :**
## Create a PostgreSQL database for the application and a new user
*!!! maybe you have to install [PostgreSQL](https://www.postgresql.org/) !!!*
Connect to PostgreSQL client, create database and new user with privileges:
```shell
$ sudo su - postgres
postgres@somewhere:~$ psql
postgres=# CREATE USER "poilaunez";
postgres=# ALTER USER projet WITH PASSWORD 'cool';
postgres=# CREATE DATABASE "db_poilaunez";
postgres=# GRANT ALL PRIVILEGES ON DATABASE db_poilaunez TO poilaunez;
postgres=# \q
postgres@somewhere:~$ exit
```
## Clone the application and install the necessary requirements
Clone the folder, go inside, create a virtual environment for Python with virtualenv (*!!! maybe you have to install [virtualenv](https://virtualenv.pypa.io/en/stable/) !!!*), use it, and install all necessary dependencies ([django](https://www.djangoproject.com/foundation/), [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/), [psycopg2](https://github.com/psycopg/psycopg2), [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)):
```shell
$ git clone https://github.com/JBthePenguin/PoilAuNezWebApp.git
$ cd PoilAuNezWebApp
$ virtualenv -p python3 env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
```
## Create tables
Make the migrations:
```shell
(env)$ python manage.py migrate
```
## Start and use the Application**
```shell
(env)$ python manage.py runserver
```
**NOW, with your favorite browser, go to this url [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and enjoy to use application.**
