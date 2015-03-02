#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import weatherometer
version = weatherometer.__version__

setup(
    name='weatherometer',
    version=version,
    author="Joe Murphy",
    author_email='jmurphy@denverpost.com',
    packages=[
        'weatherometer',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.4',
    ],
    zip_safe=False,
    scripts=['weatherometer/manage.py'],
)
