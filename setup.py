# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CESNET.
#
# CESNET OA Repository Demo is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""CESNET OpenAccess Repository demo site"""

import os

from setuptools import find_packages, setup

readme = open('README.md').read()

tests_require = []

install_requires = []

setup_requires = []

extras_require = {
    'all': []
}

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('cesnet_demo', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='oarepo-cesnet-demo',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='cesnet-demo CESNET OARepo openaccess repository demo Invenio',
    license='MIT',
    author='CESNET',
    author_email='bauer@cesnet.cz',
    url='https://github.com/oarepo/cesnet-demo',
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'cesnet-demo = invenio_app.cli:cli',
        ],
        'invenio_base.apps': [
            'cesnet_demo_records = cesnet_demo.records:OARepoDemo',
        ],
        'invenio_config.module': [
            'cesnet_demo = cesnet_demo.config',
        ],
        'invenio_base.api_apps': [
            'cesnet_demo = cesnet_demo.records:OARepoDemo',
        ],
        'invenio_jsonschemas.schemas': [
            'cesnet_demo = cesnet_demo.records.jsonschemas'
        ],
        'invenio_search.mappings': [
            'records = cesnet_demo.records.mappings'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
