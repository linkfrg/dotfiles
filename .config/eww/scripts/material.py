#!/usr/bin/python
import sys
import os
import shutil
import argparse
from jinja2 import Template
from material_color_utilities_python import *
from PIL import Image

HOME_DIR = os.getenv("HOME")
SCRIPTS_DIR = f"{HOME_DIR}/.config/eww/scripts"
CONFIG_FILE = f"{SCRIPTS_DIR}/colors/current.json"
TEMPLATES = f"{SCRIPTS_DIR}/templates"
COLORS = f"{SCRIPTS_DIR}/colors"
WALLPAPER_PATH = f"{SCRIPTS_DIR}/colors/wall.png"

# ================================COLORS=================================================

def get_colors(colorscheme):
    colors = {"primary": hexFromArgb(colorscheme.get_primary()),
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
    return colors

def get_colors_from_img(image, scheme):
    img = Image.open(image)
    basewidth = 64
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize),Image.Resampling.LANCZOS)
    theme = themeFromImage(img)
    colorscheme = theme.get('schemes').get(scheme)

    colors = get_colors(colorscheme)
    return colors

def get_colors_from_color(color, scheme):
    theme = themeFromSourceColor(argbFromHex(color))
    colorscheme = theme.get('schemes').get(scheme)
    colors = get_colors(colorscheme)
    return colors

def generate_wallpaper(color):
    img = Image.new('RGB', (1920, 1080), color)
    img.save(WALLPAPER_PATH)



# ================================SCHEME=================================================

def read_config():
    empty = {"scheme": "dark", "type": "image", "base_color": None}
    try:
        with open(CONFIG_FILE, "r") as config:
            return json.load(config)
    except FileNotFoundError:
        with open(CONFIG_FILE, "w") as config:
            json.dump(empty, config)
        return empty
    
def write_config(data):
    output_json = json.dumps(data, indent=2)
    with open(CONFIG_FILE, "w") as config:
        config.write(output_json)

# ================================GENERAL OPERATIONS=================================================

def render_templates(colors_list):
    for template in os.listdir(TEMPLATES):
        with open(f"{TEMPLATES}/{template}", "r") as file:
            template_rendered = Template(file.read()).render(colors_list)
        with open(f"{COLORS}/{template}", "w") as output_file:
            output_file.write(template_rendered)

def setup(img):
    try:
        shutil.copyfile(img, WALLPAPER_PATH)
    except shutil.SameFileError:
        pass
    os.system("pkill -SIGUSR1 kitty")
    os.system("gradience-cli apply -p ~/.config/eww/scripts/colors/colors-gradience.json --gtk both")
    os.system(f"swww img {WALLPAPER_PATH} --transition-fps 75 --transition-type wipe --transition-duration 2")

def main(colors, image, scheme, type, base_color):
    render_templates(colors)
    write_config({"scheme": scheme, "type": type, "base_color": base_color})
    setup(image)

# ================================CLI=================================================

if __name__ == "__main__":
    config = read_config()
    scheme = config['scheme']
    type = config['type']
    base_color = config['base_color']

    parser = argparse.ArgumentParser(description="Generate material colors on fly")

    parser.add_argument("--image", type=str, help="Generate color scheme based on an image file.")
    parser.add_argument("--toggle", action="store_true", help="Toggle between light and dark color schemes.")
    parser.add_argument("--current", action="store_true", help="Print current colors scheme(light/dark)")
    parser.add_argument("--color", type=str, help="Generate color scheme based on a color and simple plain wallpaper")

    args = parser.parse_args()

    if args.image:
        colors = get_colors_from_img(args.image, scheme)
        main(colors, args.image, scheme, "image", None)

    elif args.toggle:
        match scheme:
            case "dark":
                scheme = "light"
            case "light":
                scheme = "dark"
            case _:
                scheme = "dark"

        match type:
            case "image":
                colors = get_colors_from_img(WALLPAPER_PATH, scheme)
                main(colors, WALLPAPER_PATH, scheme, "image", None)

            case "color":
                colors = get_colors_from_color(base_color, scheme)
                generate_wallpaper(colors['surfaceVariant'])
                main(colors, WALLPAPER_PATH, scheme, "color", base_color)

    elif args.current:
        sys.stdout.write(scheme + "\n")
        sys.stdout.flush()

    elif args.color:
        colors = get_colors_from_color(args.color, scheme)
        generate_wallpaper(colors['secondaryContainer'])
        main(colors, WALLPAPER_PATH, scheme, "color", args.color)

    else:
        print("No valid argument specified. Use --help for usage information.")