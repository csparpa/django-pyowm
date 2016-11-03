# django-pyowm

A reusable app providing a Django ORM interface to operate with PyOWM domain entities for OWM API version 2.5


## Django support
Django 1.10+ and Python 2.7 or 3.2+


## Install

Add `django-pyowm` to the `INSTALLED_APPS` list into your Django project's `settings.py` file:
 
```python
INSTALLED_APPS = [
    ...
    'django-pyowm'  # <---
]
```


## Features
Models behave as all other Django models but they have a few useful 
functions:

  -  `<Model_class>.from_entity(entity)` - creates a PyOWM model instance
     from the corresponding PyOWM domain object instance
  -  `<Model_instance>.to_entity(entity)` - turns the model instance to
     the corresponding PyOWM domain object instance

## Usage examples

```python
# Get data an Observation from the API 
owm = OWM(API_key='my_key')
obs = owm.weather_at_place('London,UK')

# Create a model instance from API response
m = models.Observation.from_entity(obs)

# Save related objects and then the model itself
m.location.save()
m.weather.save()
m.save()

# .. or save everything in one shot
m.save_all()

# From model instance to entity
original_obs = m.to_entity()
```

## Testing
```shell
$ python runtests.py
```
