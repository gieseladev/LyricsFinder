import hashlib

from lyricsfinder.extractors.lyricsmode import Lyricsmode
from lyricsfinder.utils import UrlData


class TestLyricsMode:
    def test_can_handle(self):
        assert Lyricsmode.can_handle(UrlData("http://www.lyricsmode.com/lyrics/e/ed_sheeran/a_team_lyrics.html"))

    def test_extraction(self):
        lyrics = Lyricsmode.extract_lyrics(UrlData("http://www.lyricsmode.com/lyrics/e/ed_sheeran/a_team_lyrics.html"))

        lyrics_hash = hashlib.sha256(lyrics.lyrics.encode("utf-8")).hexdigest()

        assert lyrics_hash == "8b204bea0bb95a26066c519e88e9e9fd6174f6c24f2c2af8116f5bab111f06f4"
        assert lyrics.title == "A Team"
