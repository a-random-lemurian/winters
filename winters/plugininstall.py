from io import BytesIO
import os
import click
import json
import requests
import zipfile
import appdirs
from winters.entry import plug as app
from winters.pluginlist import get_plugins

state = {
    "yes": False
}

def should_install(should_exit=True):
    if state["yes"] is False:
        i = input("Install (y/n): ")
        if i == 'y':
            return True
        elif i == 'n':
            if should_exit:
                print("Abort")
                exit(1)
            else:
                return False
    return True

@app.command("install", help="""Install a plugin""")
@click.argument("plugin", nargs=1)
@click.option("-y/", "--yes", is_flag=True)
def install_plugin_command(plugin: str, yes):
    state["yes"] = yes
    plugins: list = json.loads(get_plugins().text)
    for plugin_obj in plugins:
        plugin_obj: dict
        if plugin.lower() in plugin_obj.get("name").lower():
            matching_plugin(plugin_obj)

def install_plugin(plugin: dict):
    url = plugin.get("url")
    print(f"Downloading {url}")
    data = requests.get(url)
    if data.status_code != 200:
        print("fatal: got error code "+data.status_code)
        exit(1)
    zip_bytesio = BytesIO(data.content)
    with zipfile.ZipFile(zip_bytesio, 'r') as zip:
        print("Files:")
        for name in zip.namelist():
            print(f"{name}")
        path = os.path.join(appdirs.user_data_dir('endless-sky'), 'plugins')
        print(f"Files will be extracted to {path}")
        if should_install():
            print(f"Extracted files to {path}")
            for zip_item in zip.namelist():
                zip.extract(zip_item, path=path)
                print(f"Extracted {os.path.join(path, zip_item)}")

def matching_plugin(plugin: dict):
    print(f"Matching plugin: {plugin.get('name')}")
    if should_install(should_exit=False):
        install_plugin(plugin)
