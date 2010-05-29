import os
from setuptools import setup, find_packages

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.rst')

setup(
    name='django-postageapp',
    version='0.1',
    description='Postageapp.com email backend for use with Django 1.2+',
    long_description=open(README_PATH).read(),
    author='Maciek Szczesniak',
    author_email='maciek@id43.net',
    url='http://bitbucket.org/vvarp/django-postageapp',
    packages=find_packages(),
    package_data={'': ['README.rst',]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
    ],
)
