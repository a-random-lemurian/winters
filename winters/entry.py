import click


@click.group()
def cli():
    pass


@cli.group()
def plug():
    pass


import winters.pluginlist

