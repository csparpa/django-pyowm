import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_pyowm',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
       'Django>=1.10.3,<2',
       'pyowm>=2.5.0,<3'
    ],
    license='MIT License',
    description='A Django ORM interface to operate with PyOWM domain entities',
    long_description=README,
    url='https://github.com/csparpa/django_pyowm',
    author='Claudio Sparpaglione',
    author_email='csparpa@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
