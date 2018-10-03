from datetime import datetime
from pathlib import Path

import pytest
from aiohttp import ClientSession

from lyricsfinder.extractors.musixmatch import MusixMatch
from lyricsfinder.models.exceptions import NoLyrics
from lyricsfinder.utils import Request

lyrics_dua_lipa_new_rules = Path("tests/data/lyrics/musixmatch-dua_lipa-new_rules.txt").read_text("utf-8")


class TestMusixMatch:
    @pytest.mark.asyncio
    async def test_can_handle(self):
        async with ClientSession() as session:
            assert await MusixMatch.can_handle(Request(session, "https://www.musixmatch.com/lyrics/Dua-Lipa/New-Rules")) is True

    @pytest.mark.xfail(raises=NoLyrics, reason="Seems like Musixmatch thinks we're a bot, pshsh what gave 'em that idea?")
    @pytest.mark.asyncio
    async def test_extraction(self):
        async with ClientSession() as session:
            lyrics = await MusixMatch.extract_lyrics(Request(session, "https://www.musixmatch.com/lyrics/Dua-Lipa/New-Rules"))

        assert lyrics.title == "New Rules"
        assert lyrics.artist == "Dua Lipa"
        assert lyrics.release_date == datetime(2017, 6, 2)
        assert lyrics.lyrics == lyrics_dua_lipa_new_rules
