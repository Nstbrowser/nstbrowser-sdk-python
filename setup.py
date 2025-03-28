import os
from setuptools import find_packages, setup

version = {}
with open(os.path.join(os.path.dirname(__file__), "nstbrowser", "_version.py")) as fp:
    exec(fp.read(), version)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name=version["__title__"],
    version=version["__version__"],
    author="nstbrowser",
    author_email="nstbrowser@gmail.com",
    description="nstbrowser python sdk",
    license="MIT",
    keywords=[
        "nstbrowser",
        "nstbrowser-sdk",
        "nstbrowser-sdk-python",
        "nst",
        "nst-sdk",
        "nst-sdk-python",
        "nstlabs",
    ],
    url="https://github.com/Nstbrowser/nstbrowser-sdk-python",
    project_urls={
        "Documentation": "https://github.com/Nstbrowser/nstbrowser-sdk-python#readme",
        "Source": "https://github.com/Nstbrowser/nstbrowser-sdk-python",
    },
    packages=find_packages(),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    install_requires=["requests"],
)
