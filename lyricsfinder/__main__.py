#!/usr/bin/env python

from argparse import ArgumentParser, Namespace

import lyricsfinder


def search(args: Namespace):
    query = " ".join(args.query)
    lyrics = next(lyricsfinder.search_lyrics(query, google_api_key=args.api_key))
    print(lyrics.lyrics)


def extract(args: Namespace):
    lyrics = lyricsfinder.extract_lyrics(args.url)
    print(lyrics.lyrics)


def main(*args):
    args = args or None

    parser = ArgumentParser("lyricsfinder", description="Find the lyrics you've always wanted to find")
    subparsers = parser.add_subparsers()

    search_parser = subparsers.add_parser("search", aliases=("s",))
    search_parser.set_defaults(func=search)
    search_parser.add_argument("api_key", help="Google Search API key")
    search_parser.add_argument("query", help="Query to search for", nargs="+")

    extract_parser = subparsers.add_parser("extract", aliases=("e",))
    extract_parser.set_defaults(func=extract)
    extract_parser.add_argument("url", help="Url to extract lyrics from")

    args = parser.parse_args(args)
    args.func(args)


if __name__ == "__main__":
    main()
