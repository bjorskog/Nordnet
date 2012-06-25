#!/usr/bin/en python

from setuptools import setup

setup(
    name='Nordnet',
    version='0.1.0',
    author='bjorskog',
    author_email='bjorn.skogtro@gmail.com',
    url='https://github.com/bjorskog/Nordnet',
    packages=['nordnet', 'nordnet.tests'],
    entry_points={
        'console_scripts':[],
        },
    test_suite='nose.collector',
    tests_require='nose',
    license='LICENSE.txt',
    description='A Python package for connecting to Nordnets API.',
    long_description=open('README.txt').read(),
    install_requires=[
        "nose >= 1.1.2"
    ],)
    
