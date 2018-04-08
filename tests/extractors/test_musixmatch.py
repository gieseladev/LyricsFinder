import hashlib
from datetime import datetime

import pytest

from lyricsfinder.extractors.musixmatch import MusixMatch
from lyricsfinder.models.exceptions import NoLyrics
from lyricsfinder.utils import UrlData


class TestMusixMatch:
    def test_can_handle(self):
        assert MusixMatch.can_handle(UrlData("https://www.musixmatch.com/lyrics/Dua-Lipa/New-Rules"))

    @pytest.mark.xfail(raises=NoLyrics, reason="Seems like Musixmatch thinks we're a bot, pshsh what gave 'em that idea?")
    def test_extraction(self):
        lyrics = MusixMatch.extract_lyrics(UrlData("https://www.musixmatch.com/lyrics/Dua-Lipa/New-Rules"))

        lyrics_hash = hashlib.sha256(lyrics.lyrics.encode("utf-8")).hexdigest()

        assert lyrics_hash == "14e75f5478b2fd7fa06a80e84fadcdbda7f33e21162116858ddecb9831a1d84b"
        assert lyrics.title == "New Rules"
        assert lyrics.artist == "Dua Lipa"
        assert lyrics.release_date == datetime(2017, 6, 2)
