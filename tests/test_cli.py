import os

import pytest

from lyricsfinder import __main__ as cli


def test_extract():
    cli.main("extract", "https://genius.com/Ed-sheeran-the-a-team-lyrics")


def test_search():
    google_api_key = os.environ.get("GOOGLE_API_KEY")
    if not google_api_key:
        pytest.skip("No google api key found (set in \"GOOGLE_API_KEY\" environment variable)")

    cli.main("search", "music", "-t", google_api_key)
    # the token should be stored and not required again
    cli.main("search", "music")
