"""Lyric finder exceptions."""


class LyricsException(Exception):
    """The base class for every lyrics exception."""

    pass


class NoExtractorError(LyricsException):
    """When there's no extractor for a url."""

    def __init__(self, url):
        """Create new."""
        super().__init__("No extractor found for {}".format(url))


class NoLyrics(LyricsException):
    """When this url doesn't point to actual lyrics."""

    pass


class NotAllowedError(LyricsException):
    """When the access is blocked."""

    pass
