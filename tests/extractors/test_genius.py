# flake8: noqa
import hashlib

from lyricsfinder.extractors.genius import Genius
from lyricsfinder.utils import UrlData


def test_can_handle():
    assert Genius.can_handle(UrlData("https://genius.com/Ed-sheeran-the-a-team-lyrics"))


def test_extraction():
    lyrics = Genius.extract_lyrics(UrlData("https://genius.com/Ed-sheeran-the-a-team-lyrics"))

    lyrics_hash = hashlib.sha256(lyrics.lyrics.encode("utf-8")).hexdigest()

    assert lyrics_hash == "8f2f9910ef8053c3b98a97c632f8ed44585b659816db94670541e3f24ca24f58"
    assert lyrics.title == "The A Team"
