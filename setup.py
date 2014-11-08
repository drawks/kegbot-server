#!/usr/bin/env python

"""Kegbot Server package.

Kegbot is a hardware and software system to record and monitor access to a
kegerator.  For more information and documentation, see http://kegbot.org/
"""

from setuptools import setup, find_packages


def setup_package():
    setup(
        name='kegbot',
        version='1.1.0',
        description=__doc__.split('\n')[0],
        long_description='\n'.join(__doc__.split('\n'))[2:],
        author='Bevbot LLC',
        author_email='info@bevbot.com',
        url='https://kegbot.org/',
        packages=find_packages(),
        scripts=[
            'bin/kegbot',
            'bin/setup-kegbot.py',
        ],
        install_requires=[
            'kegbot-pyutils == 0.1.7',
            'kegbot-api == 1.1.0',
            'Django == 1.6.6',
            'django-imagekit == 3.1',
            'django-registration == 1.0',
            'django-socialregistration == 0.5.10',
            'django-bootstrap-pagination == 0.1.10',
            'Celery == 3.1.11',
            'kombu == 3.0.16',
            'South == 0.8.4',
            'django-crispy-forms == 1.2.8',
            'foursquare == 2014.04.10',
            'gunicorn == 18.0',
            'pillow == 2.4.0',
            'protobuf == 2.5.0',
            'python-gflags == 2.0',
            'django-redis == 3.6.1',
            'pytz == 2014.2',
            'redis == 2.9.1',
            'requests == 2.2.1',
            'tweepy == 2.2',
            'jsonfield == 0.9.20',
            'protobuf == 2.5.0'],
        include_package_data=True,
        entry_points={
            'console_scripts': ['instance=django.core.management:execute_manager'],
        },
        extras_require={
            'postgres': ["psycopg2 == 2.5.4"],
            'mysql': ["MySQL-python == 1.2.5"],
        })

if __name__ == '__main__':
    setup_package()
