# flake8: noqa

import os

import lyricsfinder


def test_lyricsfinder():
    google_api_key = os.environ.get("GOOGLE_API_KEY")

    assert google_api_key

    lyrics = lyricsfinder.search_lyrics("The A Team", google_api_key=google_api_key)

    assert lyrics
