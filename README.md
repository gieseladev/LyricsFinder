[![Build Status](https://travis-ci.org/GieselaDev/LyricsFinder.svg?branch=master)](https://travis-ci.org/GieselaDev/LyricsFinder)

# LyricsFinder

LyricsFinder is a modular and easily expandable Python Package. Using a combination of a Google Custom Search Engine and a set of extractors for several sources, lyrics are attained with much higher accuracy.

### Requirements

- Python 3.6+ along with the following installed with `pip` through the `requirements.txt` file:

```
pytest
beautifulsoup4
requests
```


## Install

This package can easily be installed with `pip`:

```python
pip install lyricsfinder
```

```python
python3 -m pip install -U https://github.com/GieselaDev/LyricsFinder/archive/master.zip
```

> **From Source:**

```bash

git clone https://github.com/GieselaDev/LyricsFinder.git
cd LyricsFinder
python3 -m pip install -U -r requirements.txt

```
- **Note that** `sudo` or `sudo -H` may be required to install depending on your system setup. If any permission errors occur, please use the sudo flags.

> **Testing the package:**

Simply go to the folder where `LyricsFinder`  resides and run `pytest`  -- a successful result should appear as follows:

```bash

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

- Extractions can be performed [directly with source URL's](https://github.com/GieselaDev/LyricsFinder/blob/master/lyricsfinder/lyrics.py#L27) or with a [Google Custom Search Engine](https://github.com/GieselaDev/LyricsFinder/blob/master/lyricsfinder/lyrics.py#L53) which requires a Google Developer API key with the Search API enabled. This enables very accurate search results. Cache is also implemented for efficiency.

- Lyrics are [modeled](https://github.com/GieselaDev/LyricsFinder/blob/master/lyricsfinder/models/lyrics.py#L40) with the following base template:

```python

__slots__ = ["title", "lyrics", "origin", "timestamp"]

```
- Results can be stored in JSON format to cache. The model API takes care of this.

### Implementations

Some current implementations:

- [Giesela](https://github.com/GieselaDev/Giesela) -- a unique music suite and player for Discord.

- [GiTils](https://github.com/GieselaDev/GiTils) -- the official utilities package for Giesela, which includes an API implementation using Flask. Such an example can be seen [here](https://github.com/GieselaDev/GiTils/blob/master/GiTils/blueprints/lyrics.py).


>  An example of an output from an API implementation in action: https://utils.giesela.org/lyrics/The%20A%20Team

Lyrics are cached for faster loading. 

**[IMPORTANT] Please note that the above live example is not for large-scale use;** the public API is monitored and rate limited to prevent abuse. If you wish to host your own version, the GiTils package linked above is the implementation of the API (along with other utilities).

#### Support

Please feel free to open any issues on GitHub for questions and/or support. We're happy to help!






