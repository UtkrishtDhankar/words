#!/usr/bin/python

from setuptools import setup

setup(
    name='words',
    version = '0.1',
    packages = ['words'],
    package_data = {'words': ['data/english.txt']},
    entry_points = {'console_scripts': ['words=words.words:main']}
)
