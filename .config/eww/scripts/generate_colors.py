#!/usr/bin/python
from material_color_utilities_python import *
import sys
import os
from jinja2 import Template
from PIL import Image
from zipfile import ZipFile
import shutil

HOME_DIR=os.getenv("HOME")
SCRIPTS_DIR = f"{HOME_DIR}/.config/eww/scripts"

def get_colors(image, scheme):
    img = Image.open(image)
    basewidth = 64
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize),Image.Resampling.LANCZOS)
    theme = themeFromImage(img)

    with open(f"{SCRIPTS_DIR}/colors/current", "w") as current_theme:
        if scheme == "light":
            colorscheme = theme.get('schemes').get('light')
            current_theme.write("light")
        else:
            colorscheme = theme.get('schemes').get('dark')
            current_theme.write("dark")

    colors_list = {"primary": hexFromArgb(colorscheme.get_primary()),
                    "onPrimary": hexFromArgb(colorscheme.get_onPrimary()),
                    "primaryContainer": hexFromArgb(colorscheme.get_primaryContainer()),
                    "onPrimaryContainer": hexFromArgb(colorscheme.get_onPrimaryContainer()),
                    "secondary": hexFromArgb(colorscheme.get_secondary()),
                    "onSecondary": hexFromArgb(colorscheme.get_onSecondary()),
                    "secondaryContainer": hexFromArgb(colorscheme.get_secondaryContainer()),
                    "onSecondaryContainer": hexFromArgb(colorscheme.get_onSecondaryContainer()),
                    "tertiary": hexFromArgb(colorscheme.get_tertiary()),
                    "onTertiary": hexFromArgb(colorscheme.get_onTertiary()),
                    "tertiaryContainer": hexFromArgb(colorscheme.get_tertiaryContainer()),
                    "onTertiaryContainer": hexFromArgb(colorscheme.get_onTertiaryContainer()),
                    "error": hexFromArgb(colorscheme.get_error()),
                    "onError": hexFromArgb(colorscheme.get_onError()),
                    "errorContainer": hexFromArgb(colorscheme.get_errorContainer()),
                    "onErrorContainer": hexFromArgb(colorscheme.get_onErrorContainer()),
                    "background": hexFromArgb(colorscheme.get_background()),
                    "onBackground": hexFromArgb(colorscheme.get_onBackground()),
                    "surface": hexFromArgb(colorscheme.get_surface()),
                    "onSurface": hexFromArgb(colorscheme.get_onSurface()),
                    "surfaceVariant": hexFromArgb(colorscheme.get_surfaceVariant()),
                    "onSurfaceVariant": hexFromArgb(colorscheme.get_onSurfaceVariant()),
                    "outline": hexFromArgb(colorscheme.get_outline()),
                    "shadow": hexFromArgb(colorscheme.get_shadow()),
                    "inverseSurface": hexFromArgb(colorscheme.get_inverseSurface()),
                    "inverseOnSurface": hexFromArgb(colorscheme.get_inverseOnSurface()),
                    "inversePrimary": hexFromArgb(colorscheme.get_inversePrimary())
                }
    return colors_list

def render_templates(colors_list):
    for template in os.listdir(f"{SCRIPTS_DIR}/templates"):
        with open(f"{SCRIPTS_DIR}/templates/{template}", "r") as file:
            template_rendered = Template(file.read()).render(colors_list)
        with open(f"{SCRIPTS_DIR}/colors/{template}", "w") as output_file:
            output_file.write(template_rendered)

    os.system("pkill -SIGUSR1 kitty")


def setup(img):
    os.system("eww close wallpaper_selector")
    os.system("gradience-cli apply -p ~/.config/eww/scripts/colors/colors-gradience.json --gtk both")
    os.system(f"swww img {img} --transition-fps 75 --transition-type wipe --transition-duration 2")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if "-i" in sys.argv:
            image = sys.argv[sys.argv.index('-i') + 1]
            if "-l" in sys.argv:
                scheme = "light"
            elif "--current-scheme" in sys.argv:
                with open(f"{SCRIPTS_DIR}/colors/current", "r") as current_theme:
                    scheme = current_theme.read()
            else:
                scheme = "dark"
            colors_list = get_colors(image, scheme)
            render_templates(colors_list)
            shutil.copyfile(image, f"{SCRIPTS_DIR}/colors/wall.png")
            setup(image)
        elif "--toggle" in sys.argv:
            image = f"{SCRIPTS_DIR}/colors/wall.png"
            with open(f"{SCRIPTS_DIR}/colors/current", "r") as current_theme:
                scheme = current_theme.read()

            if scheme == "light":
                scheme = "dark"
            elif scheme == "dark":
                scheme = "light"
            else:
                scheme = "dark"

            colors_list = get_colors(image, scheme)
            render_templates(colors_list)
            setup(image)
        else:
            print(f"unknown parameter: {sys.argv[1]}")
    else:
        print("No summary specifed, try -i 'path/to/img'")