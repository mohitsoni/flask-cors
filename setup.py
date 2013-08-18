# -*- coding: utf-8 -*-

"""
Flask-CORS
----------

A flask extension to enable CORS support in flask applications. 
"""

from setuptools import setup

setup(
    name='Flask-CORS',
    version='1.0',
    url='http://github.com/mohitsoni/flask-cors',
    license='MIT',
    author='Mohit Soni',
    description='A flask extension to enable CORS support in flask applications.',
    long_description=__doc__,
    py_modules=['flask_cors'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
