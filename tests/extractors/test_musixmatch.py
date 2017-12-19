# flake8: noqa
import hashlib

from lyricsfinder.extractors.musixmatch import MusixMatch
from lyricsfinder.models.exceptions import NotAllowedError, NoLyrics
from lyricsfinder.utils import UrlData


class TestMusixmatch:
    def test_can_handle(self):
        assert MusixMatch.can_handle(UrlData("https://www.musixmatch.com/lyrics/Dua-Lipa/New-Rules"))

    def test_extraction(self):
        try:
            lyrics = MusixMatch.extract_lyrics(UrlData("https://www.musixmatch.com/lyrics/Dua-Lipa/New-Rules"))
        except (NotAllowedError, NoLyrics):
            print("Couldn't test MusixMatch, access denied or no lyrics found.")
            return

        lyrics_hash = hashlib.sha256(lyrics.lyrics.encode("utf-8")).hexdigest()

        assert lyrics_hash == "14e75f5478b2fd7fa06a80e84fadcdbda7f33e21162116858ddecb9831a1d84b"
        assert lyrics.title == "New Rules"
