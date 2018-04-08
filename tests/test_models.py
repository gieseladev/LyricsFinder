# flake8: noqa

import inspect
import json
import os
import tempfile
from contextlib import suppress
from datetime import datetime
from io import StringIO

from lyricsfinder.models import Lyrics, LyricsOrigin, exceptions


def _comp_lyrics(before: Lyrics, after: Lyrics):
    assert before.title == after.title
    assert before.artist == after.artist
    assert before.release_date == after.release_date
    assert before.lyrics == after.lyrics
    assert before.save_name == after.save_name
    assert before.origin.url == after.origin.url
    assert before.origin.source_name == after.origin.source_name
    assert before.origin.source_url == after.origin.source_url
    assert before.origin.query == after.origin.query


def test_lyrics():
    lyrics = Lyrics("lyrics title", "these are the lyrics", artist="Giesela", release_date=datetime(2008, 12, 16),
                    origin=LyricsOrigin("giesela.org/lyrics", "Giesela", "giesela.org", query="giesela lyrics"))
    assert lyrics.save_name == "giesela_lyrics.json"
    f = lyrics.save(StringIO())
    after_data = json.load(f)
    after_lyrics = Lyrics.from_dict(after_data)
    _comp_lyrics(lyrics, after_lyrics)


def test_save_lyrics():
    lyrics = Lyrics("lyrics title", "these are the lyrics", artist="Giesela", release_date=datetime(2008, 12, 16),
                    origin=LyricsOrigin("giesela.org/lyrics", "Giesela", "giesela.org", query="giesela lyrics"))
    fd, name = tempfile.mkstemp(text=True)
    try:
        lyrics.save(name).close()
        with open(name) as f:
            data = json.load(f)
        after_lyrics = Lyrics.from_dict(data)
        _comp_lyrics(lyrics, after_lyrics)
    finally:
        os.close(fd)


def test_exceptions():
    """Test whether all the exceptions derive from one base!"""
    all_exceptions = inspect.getmembers(exceptions, inspect.isclass)
    base_name, base = all_exceptions.pop(0)
    for exc_name, exc in all_exceptions:
        with suppress(base):
            raise exc("Test")
