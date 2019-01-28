If you want to use this directory for uploading medias, you have to set like Travis in settings.py and urls.py in poilaunezdjango, in all models and in db_request.

And remove all files in all folders 'migrations' except '__init__.py' before make migrations:
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate