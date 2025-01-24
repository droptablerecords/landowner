# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='landowner',
    version='0.1.0',
    description='A Python package for working with export files of your personal data from the big social media platforms.',
    long_description=readme,
    author='Loran Allen Smith',
    author_email='howdy@l13h.net',
    url='https://github.com/droptablerecords/landowner',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
