import hashlib

import pytest
from aiohttp import ClientSession

from lyricsfinder.extractors.lyricsmode import Lyricsmode
from lyricsfinder.utils import Request


class TestLyricsMode:
    @pytest.mark.asyncio
    async def test_can_handle(self):
        async with ClientSession() as session:
            assert await Lyricsmode.can_handle(Request(session, "https://www.lyricsmode.com/lyrics/e/ed_sheeran/a_team_lyrics.html")) is True

    @pytest.mark.asyncio
    async def test_extraction(self):
        async with ClientSession() as session:
            lyrics = await Lyricsmode.extract_lyrics(Request(session, "https://www.lyricsmode.com/lyrics/e/ed_sheeran/a_team_lyrics.html"))

        lyrics_hash = hashlib.sha256(lyrics.lyrics.encode("utf-8")).hexdigest()

        assert lyrics_hash == "8b204bea0bb95a26066c519e88e9e9fd6174f6c24f2c2af8116f5bab111f06f4"
        assert lyrics.title == "A Team"
        assert lyrics.artist == "Ed Sheeran"
