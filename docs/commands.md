# Commands
> [Back to list](README.md)

Documentation for commands.

# `plug`
## `ls`
**Syntax:** `winters plug ls`

Returns a list of plugins based on a file fetched [here](https://raw.githubusercontent.com/EndlessSkyCommunity/endless-sky-plugins/master/generated/plugins.json).

> `--format-style=<STYLE>`
>
> Optional argument for format style of plugin list. Supports `long` and `compact` (default).

> - `-l <LIMIT>`
> - `--limit <LIMIT>`
>
> Optional argument to limit number of items to show.

## `lslocal`
**Syntax:** `winters plug lslocal`

Returns a list of plugins installed on your computer, determined based on the folders in your Endless Sky data folder.

## `new`
**Syntax:** `winters plug new`

Creates a new plugin directory on your computer's Endless Sky data folder, and it even initialises a new Git repository by default on your computer.

> `--no-git`
> 
> Do not initialize a Git repository.

> `--no-gitignore`
>
> Do not create a `.gitignore` file. Invalid if specified with `--no-git`.