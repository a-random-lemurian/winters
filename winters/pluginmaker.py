import os
import appdirs
import click
import shutil
from winters.entry import plug as app


GIT_IGNORE_FILES = ["build/", "dist/", ".vscode/", ".DS_Store/",".winters/"]


@app.command('new')
@click.argument('name', type=str)
@click.option('--no-git',is_flag=True,help='do not initialize a git repository upon creation')
@click.option('--no-gitignore',is_flag=True,help='do not create a .gitignore file upon creation')
@click.option('--force',is_flag=True,help='overwrite plugin directory on name conflict')
def create_plugin(name, no_git, no_gitignore, force):

    if force:
        print('WARNING: use of the --force flag is DANGEROUS and may result in loss of data.')

    make_plugin_folder(name, force)

    if not no_git:
        os.system('git init')
    else:
        no_gitignore = True

    if not no_gitignore:
        make_gitignore(get_plugin_path(name))

    print('success: created plugin folder')


def get_plugin_path(name):
    return os.path.join(appdirs.user_data_dir('endless-sky'),"plugins",name)


def make_plugin_folder(name, force):
    plugin_path = get_plugin_path(name)
    if os.path.exists(plugin_path):
        if force:
            print(f'WARNING: overwriting {plugin_path} since --force was specified')
            shutil.rmtree(plugin_path)
        else:
            print('fatal: '+name+' already exists, choose a different plugin name')
            exit(1)
    os.mkdir(plugin_path)
    os.chdir(plugin_path)


def make_gitignore(plugin_path):
    with open(os.path.join(plugin_path, '.gitignore'), 'x', encoding='UTF-8') as gitignore:
        gitignore.write('\n'.join(GIT_IGNORE_FILES))
