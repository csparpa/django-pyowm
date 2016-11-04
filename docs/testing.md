# Testing

## How to run tests

As `django_pyowm` is a Django app, it must be tested against a Django project, so we will create one.

First of all you need to have the app installed in your `PYTHONPATH`.
Then create a test Django project and a test Django app with:

```shel
$ django-admin startproject testproject
$ cd testproject
$ django-admin startapp testapp
```

Then edit your `INSTALLED_APPS` in file `testproject/testproject/settings.py`

```python
INSTALLED_APPS = [
    ...
    'testapp',
    'django_pyowm'
]
```

Now copy the content of file `django_pyowm/django_pyowm/tests.py` into file `testproject/testapp/tests.py`

Apply migrations with:

```
$ cd testproject
$ python manage.py migrate
```

Finally launch the tests with:

```
$ python manage.py test
```

## Good reads
http://joebergantine.com/blog/2015/dec/03/test-reusable-django-application-support-multiple-/