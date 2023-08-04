import os

from setuptools import find_packages, setup

__DIR__ = os.path.abspath(os.path.dirname(__file__))


def requires():
    fp = open(os.path.join(__DIR__, "requirements.txt"))
    return [_.strip() for _ in fp if _.strip()]


def long_description():
    with open(os.path.join(__DIR__, "README.md")) as fp:
        return fp.read()


setup(
    name="storipy",
    version="1.0.0",
    description="Stori Challenge",
    long_description=long_description(),
    packages=find_packages(),
    include_package_data=True,
    author="Cristian Tomatis",
    author_email="cgtomatis@gmail.com",
    url="https://github.com/ctomatis/congenial-disco.git",
    python_requires=">=3.8",
    platforms=["any"],
    install_requires=requires(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
