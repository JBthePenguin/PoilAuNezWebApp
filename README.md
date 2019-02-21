[![Build Status](https://travis-ci.com/JBthePenguin/PoilAuNezWebApp.svg?branch=master)](https://travis-ci.com/JBthePenguin/PoilAuNezWebApp)
## Poil au Nez Web Application  *Django*
**This is a website like a blog with an interface admin to manage it. It's a [Django](https://www.djangoproject.com) Web application for the company of clown theater 'Poil au Nez'.
It use [GoogleDriveAPI](https://developers.google.com/drive/) to store the medias, so you have to create, in the folder *poilaunezdjango*, a file *gdriveapikey.json* with your private API Key.** (see *readme.txt* in the folder *uploads* for a local storage)
### Create a PostgreSQL database for the application and a new user
*!!! maybe you have to install [PostgreSQL](https://www.postgresql.org/) !!!*
Connect to PostgreSQL client, create database and new user with privileges:
```shell
$ sudo su - postgres
postgres@somewhere:~$ psql
postgres=# CREATE USER "poilaunez";
postgres=# ALTER USER poilaunez WITH PASSWORD 'cool';
postgres=# CREATE DATABASE "db_poilaunez";
postgres=# GRANT ALL PRIVILEGES ON DATABASE db_poilaunez TO poilaunez;
postgres=# \q
postgres@somewhere:~$ exit
```
### Clone the application and install the necessary requirements
Clone the folder, go inside, create a virtual environment for Python with virtualenv (*!!! maybe you have to install [virtualenv](https://virtualenv.pypa.io/en/stable/) !!!*), use it, and install all necessary dependencies ([django](https://www.djangoproject.com/foundation/), [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/stable/), [django-fixture-magic](https://github.com/davedash/django-fixture-magic), [django-multi-captcha-admin](https://github.com/a-roomana/django-multi-captcha-admin), [django-simple-captcha](https://django-simple-captcha.readthedocs.io/en/latest/usage.html), [django-googledrive-storage](https://django-googledrive-storage.readthedocs.io/en/latest/), [psycopg2](https://github.com/psycopg/psycopg2), [psycopg2-binary](https://pypi.org/project/psycopg2-binary/), [Pillow](https://pillow.readthedocs.io/en/stable/), [selenium](https://selenium-python.readthedocs.io/) ):
```shell
$ git clone https://github.com/JBthePenguin/PoilAuNezWebApp.git
$ cd PoilAuNezWebApp
$ virtualenv -p python3 env
$ source env/bin/activate
(env)$ pip install -r requirements.txt
```
### Create tables
```shell
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```
### Create a "superuser"
```shell
(env)$ python manage.py createsuperuser
```
### Start and use the Application
```shell
(env)$ python manage.py runserver
```
NOW, with your favorite browser, go to this url [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and for login to the admin site go to http://127.0.0.1:8000/admin/ for managing actus, galery (photos and videos) and messages. Here you can create a manager and if you want to use the custom admin site (manager), go to http://127.0.0.1:8000/manager/ and login.
### Tests
The tests use [selenium](https://selenium-python.readthedocs.io/) and maybe you have to install [GreckoWebdriver](https://github.com/mozilla/geckodriver/releases) to use firefox.
During the tests, a temporary database is creating, so you need to update the role of application:
```shell
$ sudo su - postgres
postgres@somewhere:~$ psql
postgres=# ALTER USER poilaunez CREATEDB;
postgres=# \q
postgres@somewhere:~$ exit
```
Run the tests:
```shell 
(env)$ python manage.py test -v 2
```
If you want to use Chrome, install [ChromeWebDriver](http://chromedriver.chromium.org/downloads) and update in all app's tests.py line 2:
```python
from selenium.webdriver.chrome.webdriver import WebDriver
```
###### :metal: If you want access to the custom 'error 404' page, you have to set *DEBUG = False* in *settings.py line 26*, and run the server in insecure mode:
```python
DEBUG = False
```
```shell
(env)$ python manage.py runserver --insecure
```
