#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='hublog',
    version="0.1",
    author='encorehu',
    author_email='huyoo353@126.com',
    description='a django blog',
    url='https://github.com/encorehu/hublog',
    packages=find_packages(),
    zip_safe = False,
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
