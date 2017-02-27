#!/bin/sh

mkdir -p projects/skeleton/bin
mkdir -p projects/skeleton/NAME
mkdir -p projects/skeleton/tests
mkdir -p projects/skeleton/docs

# I use a directory named projects to store all the various things I’m working on. Inside that direc- tory, I have my skeleton directory that I put the basis of my projects into. The directory NAME will be renamed to whatever you are calling your project’s main module when you use the skeleton.  Next we need to set up some initial fi les. Here’s how you do that on Linux/OSX:
touch projects/skeleton/NAME/__init__.py
touch projects/skeleton/tests/__init__.py


####
if [ -d "projects/skeleton/"  ]; then
cat << [EOF] >> projects/skeleton/setup.py
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config =[
        'description': 'My Project',
        'author': 'My Name',
        'url': 'URL to get at it.',
        'download_url': 'Where to download it.',
        'author_email':'My email.',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['NAME'],
        'scripts': [],
        'name': 'projectname'
]

setup(**config)
[EOF]
fi


###
if [ -d "projects/skeleton/tests"  ]; then
cat << [EOF] >> projects/skeleton/tests/NAME_tests.py
from nose.tools import *
import NAME

def setup():
    print "SETUP!"

def teardown():
    print "TEARDOWN!"


def test_basic():
    print "I RAN!"
[EOF]
fi
