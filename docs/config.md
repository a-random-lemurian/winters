# File paths
## Winters configuration files
Winters looks for a configuration file named `.wintersrc` in the following directories. Directories at the top of the list are searched first and are the ideal places to put Winters config files. `<USERNAME>` is replaced with your actual username. Once again, Winters relies on the Python `appdirs` library to tell it where to find the configuration file.

### Linux
- `/home/<USERNAME>/.config/winters/`
- `/home/<USERNAME>/`.

### macOS
*Same as Linux, but `/home/<USERNAME>` is replaced with `/Users/<USERNAME>`

### Windows
- `C:\Users\<USERNAME>\`

## Endless Sky data path
Winters uses the Python `appdirs` library to determine the location of your Endless Sky data. Your Endless Sky data is stored in the following directories. This is used by the `winters plug new` and `winters plug lslocal` commands.

- **Linux**: `/home/<USERNAME>/.local/share/endless-sky`
- **macOS**: `/Users/<USERNAME>/Library/Application Support/endless-sky/`
- **Windows**: `C:\Users\<USERNAME>\AppData\Roaming\endless-sky\`

# Winters configuration file
The Winters configuration file is named `.wintersrc`. The filepaths that Winters searches in is specified in the File paths section.

Configuration options have not been implemented yet, but will be implemented in a future release.