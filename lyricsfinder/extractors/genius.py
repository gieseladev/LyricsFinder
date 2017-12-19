"""Extractor for genius.com."""

import logging

from ..extractor import LyricsExtractor
from ..models.lyrics import Lyrics

log = logging.getLogger(__name__)


class Genius(LyricsExtractor):
    """Class for extracting lyrics."""

    name = "Genius"
    url = "https://genius.com/"
    display_url = "genius.com"

    @classmethod
    def extract_lyrics(cls, url_data):
        """Extract lyrics."""
        bs = url_data.bs

        lyrics_window = bs.find_all("div", {"class": "lyrics"})[0]
        lyrics = lyrics_window.text.strip()

        title = bs.find("h1", attrs={"class": "header_with_cover_art-primary_info-title"}).text.strip()

        return Lyrics(title, lyrics)
