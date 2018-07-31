import importlib
import logging
from typing import Iterator, List

from .extractor import LyricsExtractor
from .models import Lyrics, LyricsOrigin, exceptions
from .utils import UrlData, search

log = logging.getLogger(__name__)


class LyricsManager:
    """Manage stuff."""

    extractors: List[LyricsExtractor] = []

    google_api_key: str = None

    @classmethod
    def setup(cls):
        """Load extractors."""
        log.debug("setting up")
        importlib.import_module(".extractors", package=__package__)
        cls.extractors = LyricsExtractor.extractors
        log.info("loaded {} extractors".format(len(cls.extractors)))

    @classmethod
    def extract_lyrics(cls, url: str) -> Lyrics:
        """Extract lyrics from url."""
        exc = None

        log.info("extracting lyrics from url \"{}\"".format(url))
        url_data = UrlData(url)

        for extractor in cls.extractors:
            if extractor.can_handle(url_data):
                log.debug("using {} for {}".format(extractor, url_data))
                try:
                    lyrics = extractor.extract_lyrics(url_data)
                except exceptions.NoLyrics:
                    log.warning("{} didn't find any lyrics at {}".format(extractor, url))
                    continue
                except exceptions.NotAllowedError:
                    log.warning("{} couldn't access lyrics at {}".format(extractor, url))
                    continue
                except Exception as e:
                    e.__cause__ = exc
                    exc = e
                    log.exception("Something went wrong when {} handled {}".format(extractor, url_data))
                    continue
                else:
                    lyrics.set_origin(LyricsOrigin(url, extractor.name, extractor.url))
                    log.debug("extracted lyrics {}".format(lyrics))
                    return lyrics
        raise exceptions.NoExtractorError(url) from exc

    @classmethod
    def search_lyrics(cls, query: str, *, google_api_key: str = None) -> Iterator[Lyrics]:
        """Search the net for lyrics."""
        if not google_api_key:
            if cls.google_api_key:
                google_api_key = cls.google_api_key
            else:
                raise TypeError("search requires \"google_api_key\" to be present!")

        results = search(query, google_api_key)
        log.debug("got {} results".format(len(results)))
        for result in results:
            url = result["link"]
            try:
                lyrics = cls.extract_lyrics(url)
            except exceptions.NoExtractorError:
                log.warning("No extractor for url {}".format(url))
                continue
            else:
                lyrics.origin.query = query
                yield lyrics
        log.warning("No lyrics found for query \"{}\"".format(query))


LyricsManager.setup()
