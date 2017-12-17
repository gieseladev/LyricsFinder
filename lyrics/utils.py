"""Utitlities."""

import re

import requests
from bs4 import BeautifulSoup


class UrlData:
    """Url stuff."""

    def __init__(self, url):
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
    def resp(self):
        """Get the requests response object."""
        if not self._resp:
            self._resp = requests.get(self.url, headers=self.headers)
        return self._resp

    @property
    def html(self):
        """Get the html for this url."""
        if not self._html:
            self._html = self.resp.text
        return self._html

    @property
    def bs(self):
        """Get the BeautifulSoup object."""
        if not self._bs:
            self._bs = BeautifulSoup(self.html, self.html_parser)
        return self._bs


def search(query, api_key):
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


def safe_filename(name, file_ending=".json"):
    """Return a safe version of name + file_type."""
    filename = re.sub(r"\s+", "_", name)
    filename = re.sub(r"\W+", "-", filename)

    return filename.lower().strip() + file_ending
