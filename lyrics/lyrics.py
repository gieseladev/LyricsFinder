"""Fancy lyrics managment."""

import logging

from .extractor import LyricsExtractor
from .models import LyricsOrigin, exceptions
from .utils import UrlData, search

log = logging.getLogger(__name__)


class LyricsManager:
    """Manage stuff."""

    extractors = []

    google_api_key = None

    @classmethod
    def setup(cls):
        """Load extractors."""
        log.debug("setting up")
        from . import extractors  # noqa F401
        cls.extractors = LyricsExtractor.extractors
        log.info("loaded {} extractors".format(len(cls.extractors)))

    @classmethod
    def extract_lyrics(cls, url):
        """Extract lyrics from url."""
        url_data = UrlData(url)
        for extractor in cls.extractors:
            if extractor.can_handle(url_data):
                log.debug("using {} for {}".format(extractor, url_data))
                try:
                    lyrics = extractor.extract_lyrics(url_data)
                except exceptions.NoLyrics:
                    log.warn("{} didn't find any lyrics at {}".format(extractor, url))
                    continue

                if lyrics:
                    lyrics.origin = LyricsOrigin(url, extractor.name, extractor.url)
                    log.debug("extracted lyrics {}".format(lyrics))
                    return lyrics
        raise exceptions.NoExtractorError(url)

    @classmethod
    def search_lyrics(cls, query, *, google_api_key):
        """Search the net for lyrics."""
        results = search(query, google_api_key)
        log.debug("got {} results".format(len(results)))
        for result in results:
            url = result["link"]
            try:
                lyrics = cls.extract_lyrics(url)
            except exceptions.NoExtractorError:
                log.warn("No extractor for url {}".format(url))
                continue
            if lyrics:
                lyrics.origin.query = query
                return lyrics
        log.warn("No lyrics found for query \"{}\"".format(query))


LyricsManager.setup()
