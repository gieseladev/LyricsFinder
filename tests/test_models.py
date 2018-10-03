import inspect
from contextlib import suppress
from datetime import datetime

import pytest

import lyricsfinder
from lyricsfinder.models import Lyrics, LyricsOrigin, SearchResult, exceptions


def _comp_lyrics(before: Lyrics, after: Lyrics):
    assert before.title == after.title
    assert before.artist == after.artist
    assert before.release_date == after.release_date
    assert before.lyrics == after.lyrics
    assert before.origin.url == after.origin.url
    assert before.origin.source_name == after.origin.source_name
    assert before.origin.source_url == after.origin.source_url
    assert before.origin.query == after.origin.query


def test_lyrics():
    lyrics = Lyrics("lyrics title", "these are the lyrics", artist="Giesela", release_date=datetime(2008, 12, 16),
                    origin=LyricsOrigin("giesela.org/lyrics", "Giesela", "giesela.org", query="giesela lyrics"))
    after_lyrics = Lyrics.from_dict(lyrics.to_dict())
    _comp_lyrics(lyrics, after_lyrics)


def test_exceptions():
    """Test whether all the exceptions derive from one base!"""
    all_exceptions = inspect.getmembers(exceptions, inspect.isclass)
    base_name, base = all_exceptions.pop(0)
    for exc_name, exc in all_exceptions:
        with suppress(base):
            raise exc("Test")


@pytest.mark.asyncio
async def test_search_result():
    async def url_iter():
        for i in range(10):
            yield str(i)

    result = SearchResult(lyricsfinder.LyricsManager, None, url_iter(), "Test Query")

    assert await result.next_url() == "0"
    assert await result.next_url() == "1"
    assert await result.url_list() == ["2", "3", "4", "5", "6", "7", "8", "9"]
    assert await result.next_url() is None
    assert await result.next_url() is None
