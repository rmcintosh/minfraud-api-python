#!/usr/bin/env python

import ast
import codecs
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('minfraud/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(
        _version_re.search(f.read().decode('utf-8')).group(1)))

setup(name='minfraud',
      version=version,
      description='MaxMind minFraud Score and Insights API',
      long_description=__doc__,
      author='Gregory Oschwald',
      author_email='goschwald@maxmind.com',
      url='http://www.maxmind.com/',
      packages=['minfraud'],
      include_package_data=True,
      platforms='any',
      install_requires=['geoip2',
                        'requests>=2.7',
                        'rfc3987',
                        'strict-rfc3339',
                        'validate_email',
                        'voluptuous', ],
      extras_require=
      {':python_version=="2.6" or python_version=="2.7"': ['ipaddr']},
      tests_require=['requests_mock'],
      test_suite="tests",
      license='Apache License 2.0 ',
      classifiers=
      ('Development Status :: 3 - Alpha', 'Environment :: Web Environment',
       'Intended Audience :: Developers',
       'License :: OSI Approved :: Apache Software License',
       'Programming Language :: Python :: 2.6',
       'Programming Language :: Python :: 2.7',
       'Programming Language :: Python :: 3',
       'Programming Language :: Python :: 3.3',
       'Programming Language :: Python :: 3.4',
       'Programming Language :: Python', 'Topic :: Internet :: Proxy Servers',
       'Topic :: Internet :: WWW/HTTP', 'Topic :: Internet', ), )