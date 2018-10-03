import hashlib
import os

import pytest
from aiohttp import ClientSession

from lyricsfinder.extractors.azlyrics import AZLyrics
from lyricsfinder.utils import Request


class TestAZLyrics:
    @pytest.mark.asyncio
    async def test_can_handle(self):
        async with ClientSession() as session:
            assert await AZLyrics.can_handle(Request(session, "https://www.azlyrics.com/lyrics/edsheeran/theateam.html")) is True

    @pytest.mark.skipif(os.environ.get("TRAVIS") == "true", reason="AZLyrics doesn't respond to Travis' servers. Don't ask me why!")
    @pytest.mark.asyncio
    async def test_extraction(self):
        async with ClientSession() as session:
            lyrics = await AZLyrics.extract_lyrics(Request(session, "https://www.azlyrics.com/lyrics/edsheeran/theateam.html"))

        lyrics_hash = hashlib.sha256(lyrics.lyrics.encode("utf-8")).hexdigest()

        assert lyrics_hash == "e77a63fb93b1d0f373b859963532e41a2dbf2d68d290bf3f919b93b174fe26e3"
        assert lyrics.title == "The A Team"
        assert lyrics.artist == "Ed Sheeran"
