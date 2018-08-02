import hashlib
from pathlib import Path

from lyricsfinder.extractors.lyrical_nonsense import LyricalNonsense
from lyricsfinder.utils import UrlData

lyrics_sisters_umarun_taisou = Path("tests/data/lyrics/lyrical_nonsense-sisters-umarun_taisou.txt").read_text("utf-8")


class TestLyricalNonsense:
    def test_can_handle(self):
        assert LyricalNonsense.can_handle(UrlData("http://www.lyrical-nonsense.com/lyrics/radwimps/zen-zen-zense/"))

    def test_extraction(self):
        lyrics = LyricalNonsense.extract_lyrics(UrlData("http://www.lyrical-nonsense.com/lyrics/radwimps/zen-zen-zense/"))

        lyrics_hash = hashlib.sha256(lyrics.lyrics.encode("utf-8")).hexdigest()

        assert lyrics_hash == "99609e2457822377533f393eddf6c8e562d84bd376597a7272991f054c3d786c"
        assert lyrics.title == "Zenzenzense"
        assert lyrics.artist == "RADWIMPS"

        lyrics = LyricalNonsense.extract_lyrics(
            UrlData("https://www.lyrical-nonsense.com/lyrics/himouto-umaru-chan-r-theme-songs/umarun-taisou-sisters/"))

        assert lyrics.title == "Umarun Taisou"
        assert lyrics.artist == "SisterS"
        assert lyrics.lyrics == lyrics_sisters_umarun_taisou
