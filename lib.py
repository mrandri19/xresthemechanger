#! /usr/bin/python3.5
import os, click
from subprocess import run

FILE_NAME = '.Xresources'
FILE_PATH = "/home/andrea/.config/X11/"

def updateColorscheme(old_colorscheme, new_colorscheme):
    #Read from Xresources
    f = open(os.path.join(FILE_PATH, FILE_NAME), 'r+')
    content = f.read()

    #Replace the colorscheme and write
    new_content = content.replace(old_colorscheme ,new_colorscheme)

    #Clear the file before writing
    f.seek(0)
    f.truncate()
    f.write(new_content);

    #Write the backup
    old_file = open(os.path.join(FILE_PATH,'.Xresources.bak'), 'w+')
    old_file.write(content)


def findColorschemes():
    colorschemes = []
    content = os.listdir(FILE_PATH)

    #Search in the directory and create a list with the colorschemes
    for filename in content:
        if '.Xcolors' in filename:
            filename = filename.replace('.Xcolors.', '')
            filename = filename.strip(" ")
            colorschemes.append(filename + '\n')
    return colorschemes

def currentColorscheme():
    #Read from Xresources and return the third line
    f = open(os.path.join(FILE_PATH,FILE_NAME),'r')
    content = f.read()

    current = content.splitlines()[3]

    #The starting string:
    #include "/home/andrea/.config/X11/.Xcolors.XXXX"
    #return just XXXX
    current = current.replace("#include",'')\
            .replace(FILE_PATH,'')\
            .replace('.Xcolors', '')\
            .strip(" ")\
            [1:-1]\
            .strip('.')
    return current

@click.command()
@click.option('-c', '--colorscheme', help='Set the colorscheme')
@click.option('-l', '--list', help='List all the available colorschemes',\
        is_flag=True)
@click.option('--current', help='Display the current colorscheme', is_flag=True)
def cli(colorscheme, list, current):

    if colorscheme is not None :
        updateColorscheme(currentColorscheme(), colorscheme)
        #Update Xresources
        run("xrdb -load /home/andrea/.config/X11/.Xresources", shell=True, check=True)

    if list is not False:
        click.echo("".join(findColorschemes()).rstrip('\n'))

    if current is not False:
        click.echo(currentColorscheme())



if __name__ == '__main__':
    cli()
