# flake8: noqa
import hashlib

from lyricsfinder.extractors.animelyrics import Animelyrics
from lyricsfinder.utils import UrlData


class TestAnimeLyrics:
    def test_can_handle(self):
        assert Animelyrics.can_handle(UrlData("http://www.animelyrics.com/anime/swimminganime/splashfree.htm"))

    def test_extraction(self):
        lyrics = Animelyrics.extract_lyrics(UrlData("http://www.animelyrics.com/anime/swimminganime/splashfree.htm"))

        lyrics_hash = hashlib.sha256(lyrics.lyrics.encode("utf-8")).hexdigest()

        assert lyrics_hash == "f8b7b6fc53bdbc738a1b8beea09d086c6ca362c4c4857930488bc10153716dfd"
        assert lyrics.title == "SPLASH FREE"
