#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2018-present Lenovo
# Confidential and Proprietary

"""The setup script."""

from os import path
from setuptools import setup, find_packages
from pkg_resources import yield_lines

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt')) as f:
    install_requires = list(yield_lines(f.read()))

with open(path.join(here, 'test-requirements.txt')) as f:
    tests_require = list(yield_lines(f.read()))


setup(
    packages=find_packages(
        include=('lico*',)
    ),
    namespace_packages=['lico', 'lico.proxy'],
    include_package_data=True,
    install_requires=install_requires,
    test_requires=tests_require,
    zip_safe=False,
    python_requires='~=3.6',
    entry_points={
        'paste.app_factory': [
            'host = lico.proxy.filesystem.factory:create_app',
            'webdav = lico.proxy.filesystem.factory:create_webdav_app'
        ],
    }
)
