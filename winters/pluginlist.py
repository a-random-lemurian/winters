import re
import json
import requests
import click
from winters.entry import plug as app


URL_GH_ESPLUGINS = "https://raw.githubusercontent.com/EndlessSkyCommunity/endless-sky-plugins/master/generated/plugins.json"
VALID_FORMAT_STYLES = ["compact", "long"]
HEADERS = {"User-Agent": "winters | Endless Sky utility tool."}
REGEX_DETECT_GIT_COMMIT_HASH = re.compile("[abcdefABCDEF0123456789]{7,40}")


@app.command("ls")
@click.option("--format-style", default="compact")
@click.option("-l", "--limit", default=0)
def list_plugins(format_style, limit):

    if format_style not in VALID_FORMAT_STYLES:
        print("fatal: invalid format type {style}".format(style=format_style))
        return 1

    print_plugins(limit, format_style)


def get_plugins():
    return requests.get(URL_GH_ESPLUGINS, headers=HEADERS)


def print_plugins(limit, format_style):
    for plugins_listed, plugin in enumerate(json.loads(get_plugins().text), start=1):
        if plugins_listed == limit + 1 and limit != 0:
            exit()

        version = determine_version(plugin)
        authors = determine_authors(plugin)

        if format_style == "long":
            long_plugin_print(plugin, authors, version)

        if format_style == "compact":
            compact_plugin_print(plugin, authors, version)


def determine_version(plugin):
    version_info = plugin["version"]
    version = version_info
    if len(version) == 40:
        version = version_info[:7]
    return version


def determine_authors(plugin):
    authors = plugin["authors"]
    return (
        f"Multiple ({len(authors)}):" + ", ".join(authors)
        if isinstance(authors, list)
        else authors
    )


def compact_plugin_print(plugin, authors, version):
    print(f"{plugin['name']:<30}{version:<13}{authors}")


def long_plugin_print(plugin, authors, version):
    print(
        f"{plugin['name']:<30}{version:<13}{authors}"
        + "\n"
        + f"By: {authors}"
        + "\n"
        + f"{plugin['description']}"
        + "\n"
        + "-" * 40
    )


#######################################################################
