"""Searches lyrics."""

from .lyrics import LyricsManager
from .models import exceptions  # noqa: F401

extract_lyrics = LyricsManager.extract_lyrics
search_lyrics = LyricsManager.search_lyrics
