# You shouldn't change  name of function or their arguments
# ,but you can change content of the initial functions.

import json as js
import xml.etree.ElementTree as ET
from argparse import ArgumentParser
from typing import Optional, Union, Sequence

import requests


class UnhandledException(Exception):
    pass


def rss_parser(
        xml: str,
        limit: Optional[int] = None,
        json: bool = False
) -> Union[dict[str, Union[str, list]], list[str]]:
    """
    RSS parser.

    Args:
        xml: XML document as a string.
        limit: Number of the news to return. if None, returns all news.
        json: If True, format output as JSON.

    Returns:
        List of strings.
        Which then can be printed to stdout or written to file as a separate lines.

    Examples:
        xml = '<rss><channel><title>Some RSS Channel</title><link>https://some.rss.com</link><description>Some RSS Channel</description></channel></rss>'
        rss_parser(xml)
        ["Feed: Some RSS Channel",
        "Link: https://some.rss.com"]
        print("\\n".join(rss_parser(xml)))
        Feed: Some RSS Channel
        Link: https://some.rss.com
    """

    root = ET.fromstring(xml).find("channel")

    channel_tags = [
        ("Feed", "title"),
        ("Link", "link"),
        ("Last Build Date", "lastBuildDate"),
        ("Publish Date", "pubDate"),
        ("Language", "language"),
        ("Categories", "category"),
        ("Editor", "managingEditor"),
        ("Description", "description"),
    ]

    channel = {
        tag if json else output: ", ".join([cat.text for cat in root.findall(tag)])
        if tag == "category" else root.find(tag).text
        for output, tag in channel_tags if root.find(tag) is not None
    }

    item_tags = [
        ("Title", "title"),
        ("Author", "author"),
        ("Published", "pubDate"),
        ("Link", "link"),
        ("Categories", "category"),
        ("\n\n", "description"),
    ]

    items = [
        {
            tag if json else output: ", ".join([cat.text for cat in item.findall(tag)])
            if tag == "category" else item.find(tag).text
            for output, tag in item_tags if item.find(tag) is not None
        }
        for item in root.findall("item")
    ][:limit]

    output = [f"{key}: {val}" for key, val in channel.items()]
    output += "\n"
    output += [
        "\n".join([f"{key}{val}" if key == "\n\n" else f"{key}: {val}" for key, val in item.items()]) + "\n\n"
        for item in items
    ]

    channel["items"] = items
    return js.dumps(channel, indent=2) if json else output


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task."""
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided",
        type=int
    )
    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print(
            rss_parser(xml, args.limit, args.json) if args.json else "\n".join(rss_parser(xml, args.limit, args.json))
        )
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
