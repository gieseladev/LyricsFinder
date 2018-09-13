import logging

from lyricsfinder import Lyrics
from lyricsfinder.extractor import LyricsExtractor
from lyricsfinder.utils import Request

log = logging.getLogger(__name__)


class Lyricsmode(LyricsExtractor):
    name = "Lyricsmode"
    url = "http://www.lyricsmode.com/"
    display_url = "lyricsmode.com"

    @classmethod
    async def extract_lyrics(cls, request: Request) -> Lyrics:
        bs = await request.bs
        lyrics_window = bs.find_all("p", {"id": "lyrics_text", "class": "ui-annotatable"})[0]
        lyrics = lyrics_window.text

        artist_name = str(bs.select_one("a.artist_name").text)

        title = bs.find("h1", attrs={"class": "song_name fs32"}).text[len(artist_name):-7]

        artist, title = title.split("–")

        return Lyrics(title.strip(), lyrics, artist.strip())
