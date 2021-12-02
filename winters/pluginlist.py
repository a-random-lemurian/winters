import re
import json
import requests
import click
from winters.entry import plug as app


URL_GH_ESPLUGINS = "https://raw.githubusercontent.com/EndlessSkyCommunity/endless-sky-plugins/master/generated/plugins.json"
VALID_FORMAT_STYLES = ["compact", "long"]
HEADERS = {"User-Agent": "winters | Endless Sky utility tool."}
REGEX_DETECT_GIT_COMMIT_HASH = re.compile('[abcdefABCDEF0123456789]{7,40}')


@app.command('ls')
@click.option('--format-style', default="compact")
def list_plugins(format_style):
    determine_format_type(format_style)
def get_plugins():
    return requests.get(URL_GH_ESPLUGINS, headers=HEADERS)
def determine_format_type(format_style):
    if format_style not in VALID_FORMAT_STYLES:
        print('fatal: invalid format type {style}'.format(style=format_style))
        return(1)

    if format_style == 'compact':
        print_plugin_compact()
def print_plugin_compact():
    for plugin in json.loads(get_plugins().text):
        authors = plugin["authors"]
        if isinstance(authors, list):
            authors = f'Multiple ({len(authors)})'

        version = plugin["version"]
        if len(version) == 40: # It's a git commit hash.
            version = version[:7]

        print(f"{plugin['name']:<30}{version:<13}{authors}")
#######################################################################

