import hashlib

from lyricsfinder.extractors.azlyrics import AZLyrics
from lyricsfinder.utils import UrlData
import pytest
import os

key = os.getenv("proxymesh")

if key:
    proxies = {
        'http': f"http://{key}@us-ny.proxymesh.com:31280",
        'https': f"https://{key}@us-ny.proxymesh.com:31280"
    }
else:
    proxies = None


class TestAZLyrics:
    def test_can_handle(self):
        assert AZLyrics.can_handle(UrlData("https://www.azlyrics.com/lyrics/edsheeran/theateam.html", proxies=proxies))

    def test_extraction(self):
        lyrics = AZLyrics.extract_lyrics(UrlData("https://www.azlyrics.com/lyrics/edsheeran/theateam.html", proxies=proxies))

        lyrics_hash = hashlib.sha256(lyrics.lyrics.encode("utf-8")).hexdigest()

        assert lyrics_hash == "e77a63fb93b1d0f373b859963532e41a2dbf2d68d290bf3f919b93b174fe26e3"
        assert lyrics.title == "The A Team"
        assert lyrics.artist == "Ed Sheeran"
