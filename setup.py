# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='Smart-Dispatch',
    version='1.1.0',
    author='Stanislas Lauly, Marc-Alexandre Côté, Mathieu Germain',
    author_email='smart-udes-dev@googlegroups.com',
    packages=['smartdispatch'],
    scripts=['scripts/smart_dispatch.py', 'scripts/smart_worker.py'],
    url='https://github.com/SMART-Lab/smartdispatch',
    license='LICENSE.txt',
    description='A batch job launcher for the Mammouth supercomputer.',
    long_description=open('README.txt').read(),
    install_requires=[],
    package_data={'smartdispatch': ['config/*.json']}
)
