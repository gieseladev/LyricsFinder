import pytest
from aiohttp import ClientSession

from lyricsfinder import utils


# noinspection PyProtectedMember
@pytest.mark.asyncio
async def test_url_data():
    async with ClientSession() as session:
        url_data = utils.Request(session, "https://www.google.com")
        assert await url_data.bs
        assert url_data._text
        assert url_data._resp
        assert url_data._bs


def test_cleaner():
    pre = "    [allowed]|hey\n\n\nthere(test~～)    \n\tcool\r\ntest ! "
    clean = utils.clean_lyrics(pre)

    assert clean == "[allowed]hey\n\nthere(test~~)\ncool\ntest !"
