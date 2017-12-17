"""Lyric finder exceptions."""


class LyricsExceptions(Exception):
    """The base class for every lyrics exception."""

    pass


class NoExtractorError(LyricsExceptions):
    """When there's no extractor for a url."""

    def __init__(self, url):
        """Create new."""
        super().__init__("No extractor found for {}".format(url))


class NoLyrics(LyricsExceptions):
    """When this url doesn't point to actual lyrics."""

    pass
