#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name = 'steammarket',
    packages = ['steammarket'],
    version = '0.2.7',
    description = 'A Python API for getting prices from the Steam market.',
    author = 'Matyi',
    author_email = 'mmatyi@caesar.elte.hu',
    url = 'https://github.com/matyifkbt/PySteamMarket',
    download_url = 'https://github.com/matyifkbt/PySteamMarket/archive/master.zip',
    long_description = long_description,
    long_description_content_type = 'text/markdown' 
)
