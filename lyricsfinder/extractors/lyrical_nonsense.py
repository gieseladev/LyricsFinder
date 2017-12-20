"""Extractor for lyrical-nonsense.com."""

import logging

from .. import utils
from ..extractor import LyricsExtractor
from ..models.lyrics import Lyrics

log = logging.getLogger(__name__)


class LyricalNonsense(LyricsExtractor):
    """Class for extracting lyrics."""

    name = "Lyrical Nonsense"
    url = "http://www.lyrical-nonsense.com/"
    display_url = "lyrical-nonsense.com"

    @classmethod
    def extract_lyrics(cls, url_data):
        """Extract lyrics."""
        bs = url_data.bs
        lyrics_window = bs.find_all("div", {"id": "Romaji"})[0] or bs.find_all("div", {"id": "Lyrics"})[0]
        lyrics = utils.clean_lyrics(lyrics_window.contents[0])
        title = bs.select("div.titletext2new h3")[0].text.strip()

        return Lyrics(title, lyrics)
