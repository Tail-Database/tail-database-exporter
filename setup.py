#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "rt") as fh:
    long_description = fh.read()

dependencies = [
    "jsonpickle==2.2.0",
    "requests==2.28.1",
]

dev_dependencies = []

setup(
    name="tail-database-exporter",
    packages=find_packages(exclude=("tests",)),
    author="Freddie Coleman",
    author_email="f.coleman@chia.net",
    setup_requires=["setuptools_scm"],
    install_requires=dependencies,
    url="https://github.com/Tail-Database/tail-database-exporter",
    license="https://opensource.org/licenses/Apache-2.0",
    description="Exports data from Tail Database on DataLayer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Security :: Cryptography",
    ],
    extras_require=dict(
        dev=dev_dependencies,
    ),
    project_urls={
        "Bug Reports": "https://github.com/Tail-Database/tail-database-exporter",
        "Source": "https://github.com/Tail-Database/tail-database-exporter",
    },
)
