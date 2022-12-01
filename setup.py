#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from setuptools import find_packages, setup

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception as e:
    long_description = ''
    logging.exception(e)

setup(
    # Name of the package
    name='uapp',
    # Packages to include into the distribution
    packages=find_packages('.'),
    # Start with a small number and increase it with
    # every change you make https://semver.org
    version='1.2.1',
    # Chose a license from here: https: //
    # help.github.com / articles / licensing - a -
    # repository. For example: MIT.
    license='MIT',
    # Short description of your library
    description='This program tries to update all installed packages through pip.',
    # Long description of your library
    long_description=long_description,
    long_description_content_type='text/markdown',
    # Your name
    author='Lucas dSilva',
    # Your email
    author_email='accessmaker.mlbb@gmail.com',
    # Either the link to your GitHub or to your website
    url='https://github.com/accessmaker/UAPP',
    # Link from which the project can be downloaded
    download_url='https://github.com/accessmaker/UAPP.git',
    # List of keywords
    keywords=["uapp", "pip", "update"],
    # List of packages to install with this one
    install_requires=["colorama"],
    # https://pypi.org/classifiers/
    classifiers=['Development Status :: 5 - Production/Stable'],
    scripts=["uapp/bin/uapp"]
)
