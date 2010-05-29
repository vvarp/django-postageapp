import os
from setuptools import setup, find_packages

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README')

setup(
    name='django-postageapp',
    version='0.1.1a',
    description='Postageapp.com email backend for Django 1.2+',
    long_description=open(README_PATH).read(),
    author='Maciek Szczesniak',
    author_email='maciek@id43.net',
    url='http://github.com/vvarp/django-postageapp',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python',
    ],

    packages=find_packages(),
    package_data={'': ['README',]},
    package_dir={'django_postageapp': 'django_postageapp',},
    zip_safe=False,
)
