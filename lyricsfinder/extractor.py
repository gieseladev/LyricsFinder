"""Base for extracting."""

import logging

log = logging.getLogger(__name__)


class LyricsExtractorMount(type):
    """Registers new Extractors."""

    def __init__(cls, name, bases, attrs):
        """Add base class to list of extractors."""
        if not hasattr(cls, "extractors"):
            cls.extractors = []
            log.debug("Created Extractor Meta Class")
        else:
            cls.extractors.append(cls)
            log.debug("Registered Extractor \"{}\"".format(name))

    def __str__(self):
        """Return string rep."""
        return "<Extractor {}>".format(self.__name__)


class LyricsExtractor(metaclass=LyricsExtractorMount):
    """A class capable of retrieving lyrics."""

    name = "GENERIC"
    url = "http://giesela.org"
    display_url = "giesela.org"

    @classmethod
    def can_handle(cls, url_data):
        """Check whether this extractor can extract lyrics from this url."""
        return cls.display_url in url_data.url

    @classmethod
    def extract_lyrics(cls, url_data):
        """Return a Lyrics object for the given url, html or bs."""
        raise NotImplementedError
