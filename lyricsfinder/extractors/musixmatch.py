"""Extractor for Musixmatch.com."""

import logging

from ..extractor import LyricsExtractor
from ..models import exceptions
from ..models.lyrics import Lyrics

log = logging.getLogger(__name__)


class MusixMatch(LyricsExtractor):
    """Class for extracting lyrics."""

    name = "MusixMatch"
    url = "https://www.musixmatch.com/"
    display_url = "musixmatch.com"

    @classmethod
    def extract_lyrics(cls, url_data):
        """Extract lyrics."""
        url_data.headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"}
        bs = url_data.bs

        if bs.find_all("div", attrs={"class": "mxm-empty-state", "data-reactid": "87"}):
            raise exceptions.NoLyrics

        lyrics_frame = bs.find_all("div", {"class": "mxm-lyrics"})

        if not lyrics_frame:
            raise exceptions.NoLyrics

        lyrics_window = lyrics_frame[0].find_all("div", {"class": "mxm-lyrics"})

        if not lyrics_window:
            raise exceptions.NoLyrics

        lyrics_window = lyrics_window[0].span

        for garbage in bs.find_all("script"):
            garbage.replace_with(2 * "\n")

        lyrics = lyrics_window.text
        title = bs.find("h1", attrs={"class": "mxm-track-title__track"}).contents[-1].strip()

        return Lyrics(title, lyrics)
