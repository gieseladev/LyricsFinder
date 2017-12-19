[![Build Status](https://travis-ci.org/GieselaDev/LyricsFinder.svg?branch=master)](https://travis-ci.org/GieselaDev/LyricsFinder)
[![GitHub license](https://img.shields.io/github/license/GieselaDev/LyricsFinder.svg)](https://pypi.python.org/pypi/lyricsfinder)
[![Python Versions](https://img.shields.io/pypi/pyversions/lyricsfinder.svg)](https://pypi.python.org/pypi/lyricsfinder)

# LyricsFinder

LyricsFinder is a modular and easily expandable Python Package that is used to extract lyrics from music and return them in a JSON-formatted body, with abilities such as caching. By having the ability to use a combination of a Google Custom Search Engine and a set of extractors for several sources, lyrics are attained with much higher accuracy and generally from the best desired source.

### Requirements

- **Python 3.6+** with `pip` 

The following modules will be ___automatically___ downloaded and installed as part of the standard setup:

```prolog
pytest
beautifulsoup4
requests
```


## Installation 

> **This package can easily be installed with one of `pip` or `pip3` as follows:**

```bash

pip install lyricsfinder  # if pip matches Python 3.6+


pip3 install lyricsfinder # if pip3 matches Python 3.6+
``` 

**Ensure your `pip` version matches that of Python.** 

Many systems will allocate `pip3` to **Python 3.6+**, so `pip3` can be used if your system has this installed. (`pip` will, in this case, be associated with **Python 2.7.x**)



> **Alternatively, you can install directly (ensure `python3 --version` is 3.6 or greater):**

- **Note that** `sudo` or `sudo -H` may be required to install depending on your system setup. If any permission errors occur, please use the sudo flags.


```bash
python3 -m pip install -U https://github.com/GieselaDev/LyricsFinder/archive/master.zip
```

> **From Source (slower/manual way):**

```bash
$ git clone https://github.com/GieselaDev/LyricsFinder.git
$ cd LyricsFinder
$ python3 -m pip install -U -r requirements.txt
```


> **Testing the package (optional):**

Simply go to the folder where `LyricsFinder` now resides and run `pytest` -- a successful result should appear as follows:

```prolog

=========================================================================================================== test session starts ============================================================================================================
platform [your platform] -- Python 3.6.2, pytest-3.3.1, py-1.5.2, pluggy-0.6.0
rootdir: /Your/RootDirectory, inifile:
collected 5 items

tests/test_models.py .                                                                                                                                                                                                                [ 20%]
tests/test_utils.py ..                                                                                                                                                                                                                [ 60%]
tests/extractors/test_musixmatch.py ..                                                                                                                                                                                                [100%]

========================================================================================================= 5 passed in 0.73 seconds ==========================================================================================================
```



## Basic Usage

You can now import the package `lyricsfinder` as normal within your project. 

```python
import lyricsfinder

lyrics = lyricsfinder.search_lyrics("Dusk till Dawn", google_api_key="api key")
```


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

- Extractions can be performed [directly with source URL's](https://github.com/GieselaDev/LyricsFinder/blob/master/lyricsfinder/lyrics.py#L27) or with a [Google Custom Search Engine](https://github.com/GieselaDev/LyricsFinder/blob/master/lyricsfinder/lyrics.py#L53) which requires a Google Developer API key with the Search API enabled. This enables very accurate search results. Cache is also an implementation ability of the package for efficiency.

- Results can be stored in JSON format to cache, or simply returned as such. The model API takes care of this cache ability.

- The original `LyricsOrigin` model class contains the following used to initialize/construct the instance of the class:

```python

__slots__ = ["query", "url", "source_name", "source_url"]
```

- This is further converted into a `dict` (see [`to_dict`](https://github.com/GieselaDev/LyricsFinder/blob/master/lyricsfinder/models/lyrics.py#L30)) which contains the data for the source (origin) of our lyric fetch.

- Similarly, the `Lyrics` model class contains the following used to initialize/construct the instance of the class: 

```python

__slots__ = ["title", "lyrics", "origin", "timestamp"]
``` 

- This is processed and the lyric object is constructed. It is converted into a [`dict`](https://github.com/GieselaDev/LyricsFinder/blob/master/lyricsfinder/models/lyrics.py#L68) and then further processed to save to the following JSON output body: 

```json
{
  "lyrics": "", 
  "origin": {
    "query": "", 
    "source_name": "", 
    "source_url": "", 
    "url": ""
  }, 
  "timestamp": "", 
  "title": ""
}
```

- The `lyrics` contain newline parsed lyrics, the `origin` contains the `query` which was searched for, the `source_name` from one of the listed sources in the above chart (such as Genius), the `source_url` which contains the base URL of the source, and the `url` contains the direct link for the track lyrics on the given source. The `timestamp` is a standard UNIX timestamp from the request time and the `title` is the parsed title of the track in question. 

> *Please see the example of an implementation of this at the bottom of this README.*



### Implementations

Some current implementations:

- [Giesela](https://github.com/GieselaDev/Giesela) -- a unique music suite and player for Discord.

- [GiTils](https://github.com/GieselaDev/GiTils) -- the official utilities package for Giesela, which includes an API implementation using Flask. Such an example can be seen [here](https://github.com/GieselaDev/GiTils/blob/master/GiTils/blueprints/lyrics.py).


>  **An example of an output from an API implementation in action: https://utils.giesela.org/lyrics/The%20A%20Team**

Lyrics are cached for faster loading in this implementation (as is highly recommended). 

**[IMPORTANT] Please note that the above live example is not for large-scale use;** the public API is monitored and rate limited to prevent abuse. If you wish to host your own version, the GiTils package linked above is the implementation of the API (along with other utilities).

### Support

Please feel free to open any issues on GitHub for questions and/or support. We're happy to help!
