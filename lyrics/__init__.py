"""Searches lyrics."""

from .lyrics import LyricsManager
from .models import exceptions  # noqa: F401


def extract_lyrics(url):
    """Try to extract lyrics from url."""
    return LyricsManager.extract_lyrics(url)


def search_lyrics(query, *, google_api_key):
    """Search for lyrics."""
    return LyricsManager.search_lyrics(query, google_api_key)
