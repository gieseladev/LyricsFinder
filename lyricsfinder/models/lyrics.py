"""Lyrics object."""
import json
import time
from io import IOBase

from .. import utils


class LyricsOrigin:
    """Represents a place where lyrics come from."""

    __slots__ = ["query", "url", "source_name", "source_url"]

    def __init__(self, url, source_name, source_url, *, query=None):
        """Create new origin."""
        self.url = url
        self.source_name = source_name
        self.source_url = source_url
        self.query = query

    def __str__(self):
        """Return string rep."""
        return self.source_name

    @classmethod
    def from_dict(cls, data):
        """Load from dict."""
        return cls(**data)

    def to_dict(self):
        """Convert to dict."""
        return {
            "query": self.query,
            "url": self.url,
            "source_name": self.source_name,
            "source_url": self.source_url
        }


class Lyrics:
    """Represents lyrics for a song."""

    __slots__ = ["title", "lyrics", "origin", "timestamp"]

    def __init__(self, title, lyrics, *, timestamp=None):
        """Create lyrics."""
        self.title = title
        self.lyrics = lyrics
        self.origin = None

        self.timestamp = timestamp or time.time()

    def __str__(self):
        """Return string rep."""
        return "<Lyrics for \"{}\" from {}>".format(self.title, self.origin)

    @property
    def save_name(self):
        """Get a possible filename."""
        return utils.safe_filename(self.origin.query or self.title)

    @classmethod
    def from_dict(cls, data):
        """Load from dict."""
        data["origin"] = LyricsOrigin.from_dict(data["origin"])
        return cls(**data)

    def to_dict(self):
        """Convert to dict."""
        return {
            "title": self.title,
            "lyrics": self.lyrics,
            "origin": self.origin.to_dict(),
            "timestamp": self.timestamp
        }

    def save(self, f=None):
        """Save the lyrics."""
        if isinstance(f, IOBase):
            d = f
        elif isinstance(f, str):
            d = open(f, "w+")
        else:
            d = open(self.save_name, "w+")

        json.dump(self.to_dict(), d)
        d.seek(0)

        return d
