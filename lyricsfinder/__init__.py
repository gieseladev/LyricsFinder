"""Searches lyrics."""

from .lyrics import LyricsManager
from .models import exceptions  # noqa: F401


def extract_lyrics(url):
    """Try to extract lyrics from url.

    :param url: url to retrieve the lyrics from
    :returns lyricsfinder.models.lyrics.Lyrics:
    """
    return LyricsManager.extract_lyrics(url)


def search_lyrics(query, *, google_api_key):
    """Search for lyrics.

    :param query: query to search for
    :param google_api_key: api key for google custom search
    :returns lyricsfinder.models.lyrics.Lyrics:
    """
    return LyricsManager.search_lyrics(query, google_api_key=google_api_key)
