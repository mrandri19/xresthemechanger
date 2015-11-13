# xresthemechanger 
[![Build Status](https://travis-ci.org/mrandri19/xresthemechanger.svg)](https://travis-ci.org/mrandri19/xresthemechanger)

A simple python script to change the .Xresource color theme
# Usage
To install it clone the repository with `git clone https://github.com/mrandri19/xresthemechanger.git`.
Then you can just run it with `python lib.py`

# Adding to path
To call it directly from the console run this commands (assuming you are not root):
```
cp ./lib.py /usr/local/bin/
chmod +x /usr/local/bin/lib.py
```
# Configuration
To change the .Xresources path just edit the lib.py file
The variables to change are FILE_NAME and FILE_PATH

# Options
```
Usage: lib.py [OPTIONS]
Usage: xresthemechanger [OPTIONS]

Options:
  -c, --colorscheme TEXT      Set the colorscheme
  -lc, --list-colorschemes    List all the available colorschemes
  -lf, --list-fonts
  -cc, --current-colorscheme  Display the current colorscheme
  -cf, --current-font         Display the current font
  -e, --edit-xresources       Opens $EDITOR to edit the .Xresources file
  --help                      Show this message and exit.
```
#Todo
- Add file path setting directly from console
- Add a way to automatically download themes
- Add a setup file
