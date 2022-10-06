from setuptools import find_packages, setup

setup(
    name="pyprotobuf",
    version="0.0.0",
    install_requires=DEPENDENCIES,
    packages=find_packages(),
    license='Apache License, Version 2.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Ben Epstein",
    author_email="ben.epstein97@gmail.com",
    description="A dream of easy pythonic protobuf interactions",
    url="https://github.com/Ben-Epstein/pyprotobuf/"
)
