"""
https://github.com/pypa/sampleproject
http://python-packaging.readthedocs.io/en/latest/minimal.html
"""
from setuptools import setup, find_packages
from os import path

setup(
    name='wald_wolfowitz_runs_test',
    version='0.2.2',
    description='Implementation of the Wald-Wolfowitz runs test',
    long_description="The Wald-Wolfowitz runs test can be used to determine whether to sets are from the same set or not.",
    url='https://github.com/warreee/wald_wolfowitz_runs_test',
    author='Ward Schodts',
    author_email='schodtsward@gmail.com',
    license='GNU3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    install_requires=['numpy', 'scipy']

)
