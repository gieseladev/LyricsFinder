from datetime import datetime
from pathlib import Path

from lyricsfinder.extractors.genius import Genius
from lyricsfinder.utils import UrlData

lyrics_text = Path("tests/extractors/genius-ed_sheeran-the_a_team.txt").read_text("utf-8")


class TestGenius:
    def test_can_handle(self):
        assert Genius.can_handle(UrlData("https://genius.com/Ed-sheeran-the-a-team-lyrics"))

    def test_extraction(self):
        lyrics = Genius.extract_lyrics(UrlData("https://genius.com/Ed-sheeran-the-a-team-lyrics"))

        assert lyrics.lyrics == lyrics_text
        assert lyrics.title == "The A Team"
        assert lyrics.artist == "Ed Sheeran"
        assert lyrics.release_date == datetime(2011, 6, 12)
