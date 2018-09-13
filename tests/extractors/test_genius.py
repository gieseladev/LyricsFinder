from datetime import datetime
from pathlib import Path

from lyricsfinder.extractors.genius import Genius
from lyricsfinder.utils import Request
from aiohttp import ClientSession
import pytest

lyrics_text = Path("tests/data/lyrics/genius-ed_sheeran-the_a_team.txt").read_text("utf-8")


class TestGenius:
    @pytest.mark.asyncio
    async def test_can_handle(self):
        async with ClientSession() as session:
            assert await Genius.can_handle(Request(session, "https://genius.com/Ed-sheeran-the-a-team-lyrics")) is True

    @pytest.mark.asyncio
    async def test_extraction(self):
        async with ClientSession() as session:
            lyrics = await Genius.extract_lyrics(Request(session, "https://genius.com/Ed-sheeran-the-a-team-lyrics"))

        assert lyrics.lyrics == lyrics_text
        assert lyrics.title == "The A Team"
        assert lyrics.artist == "Ed Sheeran"
        assert lyrics.release_date == datetime(2011, 6, 12)
