"""
A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""


from setuptools import setup, find_packages   # Always prefer setuptools over distutils
from codecs import open     # To use a consistent encoding
from os import path

setup(
    name='setuptest',  
    version='1.0', 
    description='Testing the setup procedure',
    url='https://github.com/erelsgl/setuptest',  # Optional
    packages=find_packages(),
    install_requires=[],         # Optional
)
