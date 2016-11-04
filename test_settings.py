SECRET_KEY = 'a$h$of7!$2%a@ea=04vx(@qf^--b^4+@vmw4$@91mlxeizb2r8'
DEBUG = True,
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}
USE_TZ = True
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_pyowm'
)