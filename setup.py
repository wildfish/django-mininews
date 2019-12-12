#/usr/bin/env python

import uuid
from setuptools import setup, find_packages
from pathlib import Path

import mininews


def get_requirements(source):
    reqs = []
    with Path(source).open("r") as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            reqs.append(line)
    return reqs


setup(
    name='django-mininews',
    version=mininews.__version__,
    packages=find_packages(exclude=['example_project']),
    include_package_data=True,
    license='MIT',
    description='Boilerplate for creating publishable lists of objects',
    long_description=open('README.rst').read(),
    install_requires=get_requirements('requirements.txt'),
    url='https://github.com/richardbarran/django-mininews',
    author='Richard Barran',
    author_email='richard@arbee-design.co.uk',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
