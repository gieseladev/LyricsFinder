[![PyPI](https://img.shields.io/pypi/v/lyricsfinder.svg?longCache=false)](https://pypi.python.org/pypi/lyricsfinder)
[![Build Status](https://travis-ci.org/GieselaDev/LyricsFinder.svg?branch=master)](https://travis-ci.org/GieselaDev/LyricsFinder)
[![codecov](https://codecov.io/gh/GieselaDev/LyricsFinder/branch/master/graph/badge.svg)](https://codecov.io/gh/GieselaDev/LyricsFinder)
[![GitHub license](https://img.shields.io/github/license/GieselaDev/LyricsFinder.svg?longCache=false)](https://pypi.python.org/pypi/lyricsfinder)
[![Python Versions](https://img.shields.io/badge/python-3.7,_3.8-blue.svg?longCache=false)](https://pypi.python.org/pypi/lyricsfinder)

# LyricsFinder

LyricsFinder is a modular and easily expandable Python Package that is used to extract lyrics from music.
By having the ability to use a combination of a Google Custom Search Engine and a set of extractors for several sources,
lyrics are attained with much higher accuracy and generally from the best desired source.

### Requirements

- **Python 3.7+** with `pip`

- **[Strongly Recommended]:** A [Google Developer API Key](https://console.developers.google.com/projectselector/apis/library/customsearch.googleapis.com/) with the 'Custom Search' API enabled. This link should take one there once logged in.

*Note: While the Google tools aren't technically required for this project, much of the beneficial functionality depends on such keys/search engines. However, direct searching/parsing from a supported URL source is possible to incorporate with this package, though not the recommended way to utilize it (unless one requires a specific application requirement/design need).*


LyricsFinder uses the following packages to function:

```prolog
aiohttp
beautifulsoup4
lxml
```


## Installation

> **Note that** `sudo` may be required to install depending on your system setup. If any permission errors occur, please use the sudo flags.


> **The easiest way to install lyricsfinder is using `pip`**

```bash
pip install lyricsfinder
```

> **From Source (slower/manual way):**

```bash
$ git clone https://github.com/GieselaDev/LyricsFinder.git
$ cd LyricsFinder
$ python -m pip install .
```


> **Testing the package (optional):**

You may use [`pytest`](https://docs.pytest.org/en/latest/) to test the package. 


## Basic Usage

> **Since version 2.0.0 lyricsfinder is `async`**

You can now import the package `lyricsfinder` as normal within your project.

```python
import asyncio
import lyricsfinder

from aiohttp import ClientSession

async def main():
    async with ClientSession() as session:
        # you don't have to pass the ClientSession, lyricsfinder will create one for you
        # but if you call this function a lot it will improve performance
        lyrics_iterator = lyricsfinder.search_lyrics("Dusk till Dawn", api_key="<your google api key>", session=session)
        async for lyrics in lyrics_iterator:
            print(lyrics.title, lyrics.artist, lyrics.lyrics)

asyncio.run(main())
```

### Implementations

Some current implementations:

- [Giesela](https://github.com/GieselaDev/Giesela) -- a unique music suite and player for Discord.

- [GiTils](https://github.com/GieselaDev/GiTils) -- the official utilities package for Giesela, which includes an API implementation using Flask, uWSGI served through an optimized nginx webserver. The GiTils lyrics are stored in MongoDB cache. The example can be seen [here](https://github.com/GieselaDev/GiTils/blob/master/GiTils/blueprints/lyrics.py).


>  **An example of the live implementation of GiTils' lyrics blueprint from the source in action:** **[https://gitils.giesela.io/lyrics/substance%20therapy](https://gitils.giesela.io/lyrics/substance%20therapy)**

Lyrics are cached in MongoDB for faster loading in this implementation.

**[IMPORTANT] Please note that the above live example is not for large-scale use;** the public API is monitored and rate limited to prevent abuse. If you wish to host your own version, the GiTils package linked above is the implementation of the API (along with other utilities).

### Support

Please feel free to open any issues on GitHub for questions and/or support. We're happy to help!
