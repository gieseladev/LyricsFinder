import hashlib

from lyricsfinder.extractors.animelyrics import Animelyrics
from lyricsfinder.utils import UrlData


class TestAnimeLyrics:
    def test_can_handle(self):
        assert Animelyrics.can_handle(UrlData("http://www.animelyrics.com/anime/swimminganime/splashfree.htm"))

    def test_translated_extraction(self):
        lyrics = Animelyrics.extract_lyrics(UrlData("http://www.animelyrics.com/anime/swimminganime/splashfree.htm"))

        lyrics_hash = hashlib.sha256(lyrics.lyrics.encode("utf-8")).hexdigest()

        assert lyrics_hash == "f8b7b6fc53bdbc738a1b8beea09d086c6ca362c4c4857930488bc10153716dfd"
        assert lyrics.title == "SPLASH FREE"
        assert lyrics.artist == "STYLE FIVE"

    def test_untranslated_extraction(self):
        lyrics = Animelyrics.extract_lyrics(UrlData("https://www.animelyrics.com/anime/accelworld/chasetheworld.htm"))

        lyrics_hash = hashlib.sha256(lyrics.lyrics.encode("utf-8")).hexdigest()

        assert lyrics_hash == "3cf6a7bc4ef62cccca49e228ef556b58d459c68f4cb0dba7240cc4dffd6b3b20"
        assert lyrics.title == "Chase the world"
        assert lyrics.artist == "May'n"
