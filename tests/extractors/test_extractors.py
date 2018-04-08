from lyricsfinder.extractor import LyricsExtractor


def test_import():
    from lyricsfinder import extractors
    assert len(LyricsExtractor.extractors) == len(extractors.imported)
