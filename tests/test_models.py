# flake8: noqa

import hashlib
import json
from io import StringIO

from lyricsfinder.models import Lyrics, LyricsOrigin


def test_lyrics():
    lyrics = Lyrics("lyrics title", "these are the lyrics", origin=LyricsOrigin("giesela.org/no_lyrics", "Giesela", "giesela.org", query="giesela lyrics"))
    data = lyrics.to_dict()

    f = StringIO()
    json.dump(data, f)
    f.seek(0)

    after_data = json.load(f)

    after_lyrics = Lyrics.from_dict(after_data)

    assert lyrics.title == after_lyrics.title
    assert lyrics.lyrics == after_lyrics.lyrics
    assert lyrics.timestamp == after_lyrics.timestamp

    assert lyrics.origin.url == after_lyrics.origin.url
    assert lyrics.origin.source_name == after_lyrics.origin.source_name
    assert lyrics.origin.source_url == after_lyrics.origin.source_url
    assert lyrics.origin.query == after_lyrics.origin.query
