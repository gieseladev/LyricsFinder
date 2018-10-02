from pathlib import Path

import pytest
from aiohttp import ClientSession

from lyricsfinder.extractors.lyricsmode import Lyricsmode
from lyricsfinder.utils import Request

lyrics_ed_sheeran_a_team = Path("tests/data/lyrics/lyricsmode-ed_sheeran-a_team.txt").read_text("utf-8")


class TestLyricsMode:
    @pytest.mark.asyncio
    async def test_can_handle(self):
        async with ClientSession() as session:
            assert await Lyricsmode.can_handle(Request(session, "https://www.lyricsmode.com/lyrics/e/ed_sheeran/a_team_lyrics.html")) is True

    @pytest.mark.asyncio
    async def test_extraction(self):
        async with ClientSession() as session:
            lyrics = await Lyricsmode.extract_lyrics(Request(session, "https://www.lyricsmode.com/lyrics/e/ed_sheeran/a_team_lyrics.html"))

        assert lyrics.title == "A Team"
        assert lyrics.artist == "Ed Sheeran"
        assert lyrics.lyrics == lyrics_ed_sheeran_a_team
