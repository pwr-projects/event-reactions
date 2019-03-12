#!/bin/python

from setuptools import find_packages, setup

setup(
    name='event_reactions',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/pwr-projects/event-reactions',
    license='',
    author='Mateusz Gaweł, Grzegorz Suszka',
    # author_email='',
    description='',
    install_requires=[
        'newsapi-python',
        'tqdm'
    ]
)
