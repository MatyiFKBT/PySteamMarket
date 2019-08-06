#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'steammarket',
    packages = ['steammarket'],
    version = '0.2.1',
    description = 'A Python API for getting prices from the Steam market.',
    author = 'Matyi',
    author_email = 'mmatyi@caesar.elte.hu',
    url = 'https://github.com/matyifkbt/PySteamMarket',
    download_url = 'https://github.com/matyifkbt/PySteamMarket/archive/master.zip'
)
