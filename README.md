### Requirements
Please install the following using pip:

django

django rest-framework

django-rest-auth

django-allauth

gjango-registration

psycopg2

crispy-forms

black


### Database in settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'newsblog',
        'USER': 'postgres',
        'PASSWORD':'postgres',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

```

### Usage

Enter commands in the terminal to run app
```
$ python manage.py makemigrations
$ python manage.py migrate
```
You need to create super user to have an access to the admin panel, and after that in admin panel (localhost/admin) you also need to create User 
```
$ python manage.py createsuperuser
$ python manage.py runserver
```
### Access to API : http://127.0.0.1:8000/api.







