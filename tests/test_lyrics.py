import os

import pytest

import lyricsfinder


def test_init():
    assert lyricsfinder.search_lyrics == lyricsfinder.LyricsManager.search_lyrics
    assert lyricsfinder.extract_lyrics == lyricsfinder.LyricsManager.extract_lyrics


@pytest.mark.asyncio
async def test_lyricsfinder():
    google_api_key = os.environ.get("GOOGLE_API_KEY")
    if not google_api_key:
        pytest.skip("No google api key found (set in \"GOOGLE_API_KEY\" environment variable)")
    lyrics = await lyricsfinder.search_lyrics("The A Team", api_key=google_api_key).__anext__()
    assert lyrics


@pytest.mark.asyncio
async def test_extraction():
    urls = [
        "http://www.animelyrics.com/anime/haruhi/harehareyukaiemiri.htm"
    ]
    for url in urls:
        await lyricsfinder.extract_lyrics(url)
