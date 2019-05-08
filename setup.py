import os
from setuptools import setup
from distutils.core import Command


setup(
    name='la-election-night',
    version='0.0.3',
    description="Parse historical and election night result files published by the Los Angeles County Registrar-Recorder/County Clerk",
    author='Los Angeles Times Data Desk',
    author_email='datadesk@latimes.com',
    url='http://www.github.com/datadesk/la-election-night',
    license="MIT",
    packages=("la_election_night",),
    include_package_data=True,
    zip_safe=False,  # because we're including static files
    install_requires=("requests",),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
)
