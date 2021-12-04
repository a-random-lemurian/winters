import os
import appdirs
import click
from winters.entry import plug as app


GIT_IGNORE_FILES = ["build/", "dist/", ".vscode/", ".DS_Store/",".winters/"]


@app.command('new')
@click.argument('name', type=str)
@click.option('--no-git',is_flag=True,help='do not initialize a git repository upon creation')
@click.option('--no-gitignore',is_flag=True,help='do not create a .gitignore file upon creation')
def create_plugin(name, no_git, no_gitignore):
    make_plugin_folder(name)

    if not no_git:
        os.system('git init')
        no_gitignore = True

    if not no_gitignore:
        make_gitignore(get_plugin_path(name))

    print('success: created plugin folder')


def get_plugin_path(name):
    return os.path.join(appdirs.user_data_dir('endless-sky'),"plugins",name)


def make_plugin_folder(name):
    plugin_path = get_plugin_path(name)
    if os.path.exists(plugin_path):
        print('fatal: '+name+' already exists, choose a different plugin name')
        exit(1)
    os.mkdir(plugin_path)
    os.chdir(plugin_path)


def make_gitignore(plugin_path):
    with open(os.path.join(plugin_path, '.gitignore'), 'w', encoding='utf8') as gitignore:
        gitignore.write('\n'.join(GIT_IGNORE_FILES))
