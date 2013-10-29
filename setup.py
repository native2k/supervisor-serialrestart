#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='supervisorserialrestart',
    version='0.1.0',
    description='Adds serialrestart command to Supervisor.',
    long_description=readme + '\n\n' + history,
    author='Sven Richter',
    author_email='native2k@gmail.com',
    url='https://github.com/native2k/supervisorserialrestart',
    packages=[
        'supervisorserialrestart',
    ],
    package_dir={'supervisorserialrestart': 'supervisorserialrestart'},
    include_package_data=True,
    install_requires=[
    ],
    license="BSD",
    zip_safe=False,
    keywords='supervisorserialrestart',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests.run_tests.run_all',
)