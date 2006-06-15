#!/usr/bin/env python
"""Distutils setup file"""

import ez_setup
ez_setup.use_setuptools()
from setuptools import setup

# Metadata
PACKAGE_NAME = "PEAK-Rules"
PACKAGE_VERSION = "0.1"
PACKAGES = ['peak', 'peak.rules']

def get_description():
    # Get our long description from the documentation
    f = file('README.txt')
    lines = []
    for line in f:
        if not line.strip():
            break     # skip to first blank line
    for line in f:
        if line.startswith('.. contents::'):
            break     # read to table of contents
        lines.append(line)
    f.close()
    return ''.join(lines)

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description="Generic functions and business rules support systems",
    long_description = get_description(),
    install_requires=['BytecodeAssembler>=0.0.2.dev-r2188','DecoratorTools>=1.0'],
    author="Phillip J. Eby",
    author_email="peak@eby-sarna.com",
    license="PSF or ZPL",
    #url="http://peak.telecommunity.com/DevCenter/PEAK-Rules",
    test_suite = 'test_rules',
    packages = PACKAGES,
    namespace_packages = ['peak'],
)

