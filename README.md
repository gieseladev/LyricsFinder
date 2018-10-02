[![PyPI](https://img.shields.io/pypi/v/lyricsfinder.svg?longCache=false)](https://pypi.python.org/pypi/lyricsfinder)
[![Build Status](https://travis-ci.org/GieselaDev/LyricsFinder.svg?branch=master)](https://travis-ci.org/GieselaDev/LyricsFinder)
[![codecov](https://codecov.io/gh/GieselaDev/LyricsFinder/branch/master/graph/badge.svg)](https://codecov.io/gh/GieselaDev/LyricsFinder)
[![GitHub license](https://img.shields.io/github/license/GieselaDev/LyricsFinder.svg?longCache=false)](https://pypi.python.org/pypi/lyricsfinder)
[![Python Versions](https://img.shields.io/badge/python-3.6,_3.7-blue.svg?longCache=false)](https://pypi.python.org/pypi/lyricsfinder)

# LyricsFinder

LyricsFinder is a modular and easily expandable Python Package that is used to extract lyrics from music. By having the ability to use a combination of a Google Custom Search Engine and a set of extractors for several sources, lyrics are attained with much higher accuracy and generally from the best desired source.

### Requirements

- **Python 3.6+** with `pip`

- **[Strongly Recommended]:** A [Google Developer API Key](https://console.developers.google.com/projectselector/apis/library/customsearch.googleapis.com/) with the 'Custom Search' API enabled. This link should take one there once logged in.

*Note: While the Google tools aren't technically required for this project, much of the beneficial functionality depends on such keys/search engines. However, direct searching/parsing from a supported URL source is possible to incorporate with this package, though not the recommended way to utilize it (unless one requires a specific application requirement/design need).*


The following modules will be ___automatically___ downloaded and installed as part of the standard setup:

```prolog
beautifulsoup4
requests
```


## Installation


> **Note that** `sudo` may be required to install depending on your system setup. If any permission errors occur, please use the sudo flags.


> **This package can easily be installed with one of `pip` or `pip3` as follows:**

```bash

pip install lyricsfinder  # if pip matches Python 3.6+


pip3 install lyricsfinder # if pip3 matches Python 3.6+

```

**Ensure your `pip` version matches that of Python.**

Many systems will allocate `pip3` to **Python 3.x+**, so `pip3` can be used if your system has this installed. (`pip` will, in this case, be associated with **Python 2.7.x**)



> **Alternatively, you can install directly (ensure `python3 --version` is 3.6 or greater):**

```bash
python3 -m pip install -U https://github.com/GieselaDev/LyricsFinder/archive/master.zip
```

> **From Source (slower/manual way):**

```bash
$ git clone https://github.com/GieselaDev/LyricsFinder.git
$ cd LyricsFinder
$ python3 -m pip install .
```


> **Testing the package (optional):**

You may use [`pytest`](https://docs.pytest.org/en/latest/) to test the package. 


## Basic Usage

You can now import the package `lyricsfinder` as normal within your project.

```python
import lyricsfinder

lyrics = lyricsfinder.search_lyrics("Dusk till Dawn", google_api_key="api key")
```
`lyrics` is a `Lyrics` instance (see below).


## Expandability / Design

LyricsFinder is designed with expandability in mind. The following is a very brief structure of the project:

| Source | Description |
| --- | --- |
| Anime Lyrics  | Extractor for animelyrics.com |
| AZLyrics | Extractor for azlyrics.com |
| Genius | Extractor for genius.com |
| Lyricsmode  | Extractor for lyricsmode.com |
| Lyrical Nonsense | Extractor for lyrical-nonsense.com |
| Musixmatch | Extractor for musixmatch.com |

- Extractions can be performed [directly with source URL's](https://github.com/GieselaDev/LyricsFinder/blob/master/lyricsfinder/lyrics.py#L27) or with a [Google Custom Search Engine](https://github.com/GieselaDev/LyricsFinder/blob/master/lyricsfinder/lyrics.py#L53) which requires a Google Developer API key with the Search API enabled. This enables very accurate search results.

- Results can be stored in JSON format to cache by using `json.dump` on the dict that is returned by calling `to_dict()`.

- The [following contains the base model for the Lyrics Object](https://github.com/GieselaDev/LyricsFinder/blob/master/lyricsfinder/models/lyrics.py) -- within it we have our class structures for the `LyricsOrigin` and `Lyrics` classes, which we discuss below.

---------


- The original `LyricsOrigin` model class contains the following attributes:
   `query`, `url`, `source_name`, `source_url`


- Similarly, the `Lyrics` model class contains the following attributes:
   `title`, `lyrics`, `origin`, `timestamp`

- The `lyrics` contain newline parsed lyrics, the `origin` contains the `query` which was searched for, the `source_name` from one of the listed sources in the above chart (such as Genius), the `source_url` which contains the base URL of the source, and the `url` contains the direct link for the track lyrics on the given source. The `timestamp` is a standard UNIX timestamp from the request time and the `title` is the parsed title of the track in question.

> *Please see the example of an implementation of this at the bottom of this README.*



### Implementations

Some current implementations:

- [Giesela](https://github.com/GieselaDev/Giesela) -- a unique music suite and player for Discord.

- [GiTils](https://github.com/GieselaDev/GiTils) -- the official utilities package for Giesela, which includes an API implementation using Flask, uWSGI served through an optimized nginx webserver. The GiTils lyrics are stored in MongoDB cache. The example can be seen [here](https://github.com/GieselaDev/GiTils/blob/master/GiTils/blueprints/lyrics.py).


>  **An example of the live implementation of GiTils' lyrics blueprint from the source in action:** **[https://gitils.giesela.io/lyrics/substance%20therapy](https://gitils.giesela.io/lyrics/substance%20therapy)**

Lyrics are cached in MongoDB for faster loading in this implementation.

**[IMPORTANT] Please note that the above live example is not for large-scale use;** the public API is monitored and rate limited to prevent abuse. If you wish to host your own version, the GiTils package linked above is the implementation of the API (along with other utilities).

### Support

Please feel free to open any issues on GitHub for questions and/or support. We're happy to help!
