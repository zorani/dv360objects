# from distutils.core import setup
##How to package
##From your root package dir...
##python3 setup.py sdist
##twine check dist/*
##twine upload dist/*


from setuptools import setup

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="dv360objects",
    packages=[
        "dv360objects",
        "dv360objects.common",
        "dv360objects.dv360api",
        "dv360objects.dv360object",
    ],
    version="0.0.1",
    license="MIT",
    description="Saturation work",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="zoran ilievski",
    author_email="pythonic@clientuser.net",
    url="https://github.com/zorani/dv360objects",
    download_url="https://github.com/zorani/dv360objects/archive/refs/tags/v0.0.1.tar.gz",
    keywords=["dv360"],
    install_requires=["cloudapi>=1.1.2", "Jettings"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
