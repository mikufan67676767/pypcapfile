#!/usr/bin/env python

import os
from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="pypcapfile",
    version="0.12.1",
    description="Pure Python package for reading and parsing libpcap savefiles",
    long_description=read("README.rst"),
    author="mikufan67676767",
    author_email="256880237+mikufan67676767@users.noreply.github.com",
    license="ISC",
    url="https://github.com/mikufan67676767/pypcapfile",
    scripts=["pcapfile_info", "helper.py"],
    packages=[
        "pcapfile",
        "pcapfile.test",
        "pcapfile.protocols",
        "pcapfile.protocols.linklayer",
        "pcapfile.protocols.network",
        "pcapfile.protocols.transport",
    ],
    package_data={"pcapfile.test": ["test/test_data"]},
    data_files=[("share/doc/pcapfile", ["README.rst", "AUTHORS", "CONTRIBUTING"])],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
