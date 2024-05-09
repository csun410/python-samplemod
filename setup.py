# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python',
    long_description=readme,
    author='Author',
    author_email='author@example.com',
    url='https://example.com/python-samplemod',
    packages=find_packages(exclude=('tests', 'docs'))
)

