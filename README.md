# xresthemechanger
A simple python script to change the .Xresource color theme
# Usage
To install it clone the repository with `git clone https://github.com/mrandri19/xresthemechanger.git`.
Then you can just run it with `python lib.py`
# Dependencies
It require [Python](https://www.python.org/) > 3 and
[Click](http://click.pocoo.org/5/) ~ 5.0
Install it using pip with `pip install click`
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
xresthemechanger --help
Usage: xresthemechanger [OPTIONS]

Options:
  -c, --colorscheme TEXT  Set the colorscheme
  -l, --list              List all the available colorschemes
  --current               Display the current colorscheme
  --help                  Show this message and exit.
```
#Todo
- Add file path setting directly from console
- Add a way to automatically download themes
- Add a setup file
