from setuptools import setup, find_packages

setup(
    name="crime_test",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy"
    ],
    description="A package for validating and analyzing crime data",
    author="Aaminah Mohammad",
    author_email="aaminah@example.com"
)

