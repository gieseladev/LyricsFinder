# flake8: noqa

from .lyrics import LyricsManager


def extract_lyrics(url):
    return LyricsManager.extract_lyrics(url)


def search_lyrics(query, *, google_api_key):
    return LyricsManager.search_lyrics(query, google_api_key)
