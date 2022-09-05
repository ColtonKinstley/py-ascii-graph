#!/usr/bin/env python
import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

description = 'A simple python lib to print data as ascii histograms.'

try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'),
              encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = description

try:
    with open(os.path.join(os.path.dirname(__file__), 'LICENSE'), encoding='utf-8') as f:
        license = f.read()
except Exception:
    license = 'MIT'


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='ascii_graph',
    version='1.5.2',
    author='Pierre-Francois Carpentier',
    author_email='coltonkinstley@gmail.com',
    packages=['ascii_graph'],
    scripts=['scripts/asciigraph'],
    url='https://github.com/coltonkinstley/py-ascii-graph',
    license=license,
    description=description,
    long_description=long_description,
    install_requires=[],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 4 - Beta', 'Intended Audience :: System Administrators',
        'Intended Audience :: Developers', 'Environment :: Console',
        'License :: OSI Approved :: MIT License', 'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3.5', 'Programming Language :: Python :: 3.6'
        'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8'
        'Programming Language :: Python :: 3.9', 'Programming Language :: Python :: 3.10'
    ])
