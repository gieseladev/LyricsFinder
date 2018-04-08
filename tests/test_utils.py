from lyricsfinder import utils


def test_safe_filename():
    assert utils.safe_filename("What's the matter", ".json") == "what-s_the_matter.json"


def test_url_data():
    """Test whether the UrlData class caches properly."""
    url_data = utils.UrlData("https://www.google.com")
    assert url_data.bs
    assert url_data._html
    assert url_data._resp
    assert url_data._bs


def test_cleaner():
    pre = "    [allowed]|hey\n\n\nthere(test)    \n\tcool\r\ntest ! "
    clean = utils.clean_lyrics(pre)

    assert clean == "[allowed]hey\n\nthere(test)\ncool\ntest !"
