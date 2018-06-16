import hashlib
from datetime import datetime

from lyricsfinder.extractors.genius import Genius
from lyricsfinder.utils import UrlData


class TestGenius:
    def test_can_handle(self):
        assert Genius.can_handle(UrlData("https://genius.com/Ed-sheeran-the-a-team-lyrics"))

    def test_extraction(self):
        lyrics = Genius.extract_lyrics(UrlData("https://genius.com/Ed-sheeran-the-a-team-lyrics"))

        lyrics_hash = hashlib.sha256(lyrics.lyrics.encode("utf-8")).hexdigest()

        assert lyrics_hash == "abebd9158717ba25ecba32725e6f517837ff5280b55544b576e6e3f3d7f1b590"
        assert lyrics.title == "The A Team"
        assert lyrics.artist == "Ed Sheeran"
        assert lyrics.release_date == datetime(2011, 6, 12)
