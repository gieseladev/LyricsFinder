"""Extractor for animelyrics.com."""

import logging
import re

import requests

from ..extractor import LyricsExtractor
from ..models.lyrics import Lyrics

log = logging.getLogger(__name__)


class Animelyrics(LyricsExtractor):
    """Class for extracting lyrics."""

    name = "Animelyrics"
    url = "http://www.animelyrics.com/"
    display_url = "animelyrics.com"

    @classmethod
    def extract_lyrics(cls, url_data):
        """Extract lyrics."""
        bs = url_data.bs

        main_body = bs.find_all("table")[0]
        lyrics_window = main_body.find_all("table")

        if lyrics_window:  # shit's been translated
            lyrics_window = lyrics_window[0]

            lines = lyrics_window.find_all("tr")
            lyrics = ""
            for line in lines:
                p = line.td
                if p:
                    p.span.dt.replace_with("")
                    for br in p.span.find_all("br"):
                        br.replace_with("\n")

                    lyrics += p.span.text
            lyrics = lyrics.strip()
        else:
            raw = requests.get(re.sub(r"\.html?", ".txt", url_data.url), allow_redirects=False)
            content = raw.text.strip()
            match = re.search(r"-{10,}(.+?)-{10,}", content, flags=re.DOTALL)
            if match:
                lyrics = match.group(1).strip()

        title = bs.find("td", attrs={"valign": "top"}).find("h1").text.strip()

        return Lyrics(title, lyrics)
