"""Utitlities."""

import re
from typing import List

import requests
from bs4 import BeautifulSoup
from requests import Response


class UrlData:
    """Url stuff."""

    def __init__(self, url: str):
        """Build url."""
        self.url = url
        self.headers = {}

        self.html_parser = "html.parser"

        self._resp = None
        self._html = None
        self._bs = None

    def __str__(self):
        """Return string rep."""
        return "<{}>".format(self.url)

    @property
    def resp(self) -> Response:
        """Get the requests response object."""
        if not self._resp:
            self._resp = requests.get(self.url, headers=self.headers)
        return self._resp

    @property
    def html(self) -> str:
        """Get the html for this url."""
        if not self._html:
            self._html = self.resp.text
        return self._html

    @property
    def bs(self) -> BeautifulSoup:
        """Get the BeautifulSoup object."""
        if not self._bs:
            self._bs = BeautifulSoup(self.html, self.html_parser)
        return self._bs


def search(query: str, api_key: str) -> List:
    """Return search results."""
    params = {
        "key": api_key,
        "cx": "002017775112634544492:7y5bpl2sn78",
        "q": query
    }
    resp = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
    data = resp.json()
    items = data.get("items", [])
    return items


def safe_filename(name: str, file_ending: str = ".json") -> str:
    """Return a safe version of name + file_type."""
    filename = re.sub(r"\s+", "_", name)
    filename = re.sub(r"\W+", "-", filename)

    return filename.lower().strip() + file_ending


def clean_lyrics(lyrics: str) -> str:
    """Perform some simple operations to clean the lyrics."""
    lyrics = lyrics.strip()
    lyrics = re.sub(r"[^\w\[\]()/ \"',\.:\-\n?!]+", "", lyrics)  # remove unwanted characters
    lyrics = re.sub(r" +", " ", lyrics)  # reduce to one space only
    lyrics = re.sub(r"\n{2,}", "\n\n", lyrics)  # reduce to max 2 new lines in a row
    lyrics = re.sub(r" +?\n", "\n", lyrics)  # remove space before newline

    return lyrics
