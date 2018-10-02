from pathlib import Path

import pytest
from aiohttp import ClientSession

from lyricsfinder.extractors.lyrical_nonsense import LyricalNonsense
from lyricsfinder.utils import Request

lyrics_sisters_umarun_taisou = Path("tests/data/lyrics/lyrical_nonsense-sisters-umarun_taisou.txt").read_text("utf-8")
lyrics_radwimps_zenzenzense = Path("tests/data/lyrics/lyrical_nonsense-radwimps-zenzenzense.txt").read_text("utf-8")


class TestLyricalNonsense:
    @pytest.mark.asyncio
    async def test_can_handle(self):
        async with ClientSession() as session:
            assert await LyricalNonsense.can_handle(Request(session, "http://www.lyrical-nonsense.com/lyrics/radwimps/zen-zen-zense/")) is True

    @pytest.mark.asyncio
    async def test_extraction(self):
        async with ClientSession() as session:
            lyrics = await LyricalNonsense.extract_lyrics(Request(session, "http://www.lyrical-nonsense.com/lyrics/radwimps/zen-zen-zense/"))

        assert lyrics.title == "Zenzenzense"
        assert lyrics.artist == "RADWIMPS"
        assert lyrics.lyrics == lyrics_radwimps_zenzenzense

        async with ClientSession() as session:
            lyrics = await LyricalNonsense.extract_lyrics(
                Request(session, "https://www.lyrical-nonsense.com/lyrics/himouto-umaru-chan-r-theme-songs/umarun-taisou-sisters/"))

        assert lyrics.title == "Umarun Taisou"
        assert lyrics.artist == "SisterS"
        assert lyrics.lyrics == lyrics_sisters_umarun_taisou
