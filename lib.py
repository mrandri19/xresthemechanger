#! /usr/bin/python3.5
import os
import click
from subprocess import run

FILE_NAME = '.Xresources'
FILE_PATH = "/home/andrea/.config/X11/"


def getFile(mode):
    # Read from Xresources
    f = open(os.path.join(FILE_PATH, FILE_NAME), mode)
    return f.read()


def updateColorscheme(old_colorscheme, new_colorscheme):

    f = open(os.path.join(FILE_PATH, FILE_NAME), 'r+')
    content = getFile('r+')

    # Replace the colorscheme and write
    new_content = content.replace(old_colorscheme, new_colorscheme)

    # Clear the file before writing
    f.seek(0)
    f.truncate()
    f.write(new_content)

    # Write the backup
    old_file = open(os.path.join(FILE_PATH, '.Xresources.bak'), 'w+')
    old_file.write(content)


def findColorschemes():
    colorschemes = []
    content = os.listdir(FILE_PATH)

    # Search in the directory and create a list with the colorschemes
    for filename in content:
        if '.Xcolors' in filename:
            filename = filename.replace('.Xcolors.', '')
            filename = filename.strip(" ")
            colorschemes.append(filename + '\n')
    return colorschemes


def currentColorscheme():
    # Read from Xresources and return the third line
    content = getFile('r')

    lines = content.splitlines()
    for line in lines:
        if ".Xcolors" in line:
            # The starting string:
            # include "/home/andrea/.config/X11/.Xcolors.XXXX"
            # return just XXXX
            line = line.replace("#include", '')\
                .replace(FILE_PATH, '')\
                .replace('.Xcolors', '')\
                .strip(" ")[1:-1]\
                .strip('.')
            return line
    return False


def currentFont():
    fonts = []

    content = getFile('r')

    lines = content.splitlines()
    for line in lines:
        if "URxvt.font" in line:
            # The starting string
            # URxvt.font : xft:Ubuntu Mono derivative Powerline:size=12
            # The final Ubuntu Mono derivative Powerline
            line = line.replace("URxvt.font :", "")
            line = line.replace("!", "")
            line = line.replace("xft:", "")
            line = line.split(":")[0]
            line = line.strip()
            line += "\n"
            fonts.append(line)
    return fonts


@click.command()
@click.option('-c', '--colorscheme', help='Set the colorscheme')
@click.option('-lc', '--list-colorschemes',
              help='List all the available colorschemes',
              is_flag=True)
@click.option('-cc', '--current-colorscheme',
              help='Display the current colorscheme',
              is_flag=True)
@click.option('-cf', '--current-font', help='Display the current font',
              is_flag=True)
@click.option('-e', '--edit-xresources',
              help='Opens $EDITOR to edit the .Xresources file', is_flag=True)
def cli(colorscheme, list_colorschemes, current_colorscheme, current_font,
        edit_xresources):

    if colorscheme is not None:
        updateColorscheme(currentColorscheme(), colorscheme)
        # Update Xresources
        run("xrdb -load {}{}".format(FILE_PATH, FILE_NAME), shell=True,
            check=True)

    if list_colorschemes is True:
        click.echo("".join(findColorschemes()).rstrip("\n"))

    if current_colorscheme is True:
        click.echo(currentColorscheme())

    if current_font is True:
        click.echo("".join(currentFont()).rstrip("\n"))

    if edit_xresources is True:
        os.system('{} {}'.format(os.getenv('EDITOR'), (FILE_PATH+FILE_NAME)))

    # No arguments
    if colorscheme is None and not list_colorschemes and not current_colorscheme\
            and not current_font and not edit_xresources:
                click.echo("Usage:")

if __name__ == "__main__":
    cli()
