"""Setup for this stuff."""

from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="lyricsfinder",
    version="1.0.3",
    description="Retrieve lyrics for a song",
    long_description=long_description,
    url="https://github.com/siku2/LyricsFinder",
    author="siku2",
    author_email="siku2@outlook.com",
    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio",

        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6"
    ],
    keywords="lyrics",
    packages=find_packages(exclude=["docs", "tests"]),
    install_requires=["beautifulsoup4", "requests"]
)
