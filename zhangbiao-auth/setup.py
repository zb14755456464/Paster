#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2019-present Lenovo
# Confidential and Proprietary

from os import path
from setuptools import setup, find_packages
from pkg_resources import yield_lines

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt')) as f:
    install_requires = list(yield_lines(f.read()))

with open(path.join(here, 'test-requirements.txt')) as f:
    tests_require = list(yield_lines(f.read()))

setup(
    namespace_packages=['lico'],
    packages=find_packages(
        include=[
            'lico*'
        ],
    ),
    zip_safe=True,
    include_package_data=True,
    install_requires=install_requires,
    python_requires='>=2.7',
    tests_require=tests_require,
    entry_points={
        'paste.filter_factory': [
            'main = lico.auth.paste:service_auth_filter_factory'
        ],
    },
)
