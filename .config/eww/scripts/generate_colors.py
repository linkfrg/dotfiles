#!/usr/bin/python
from material_color_utilities_python import *
import sys
import os
from jinja2 import Template
from PIL import Image
import shutil

from PIL import Image, ImageDraw, ImageFont
import random

HOME_DIR=os.getenv("HOME")
SCRIPTS_DIR = f"{HOME_DIR}/.config/eww/scripts"
CONFIG_FILE = f"{SCRIPTS_DIR}/colors/current.json"

def get_colors_from_img(image, scheme):
    img = Image.open(image)
    basewidth = 64
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize),Image.Resampling.LANCZOS)
    theme = themeFromImage(img)
    colorscheme = theme.get('schemes').get(scheme)

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

def get_colors_from_color(color, scheme):
    theme = themeFromSourceColor(argbFromHex(color))
    colorscheme = theme.get('schemes').get(scheme)

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
    try:
        shutil.copyfile(img, f"{SCRIPTS_DIR}/colors/wall.png")
    except shutil.SameFileError:
        pass
    os.system("gradience-cli apply -p ~/.config/eww/scripts/colors/colors-gradience.json --gtk both")
    os.system(f"swww img {img} --transition-fps 75 --transition-type wipe --transition-duration 2")


def emoji_wallpaper(colors_list):

    # Set image size and background color
    width, height = 1920, 1080
    background_color = colors_list['surface']

    # Create a new image with the specified background color
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Define a list of emojis
    emojis = ["", "󰳗", "󰣐", "󰞅", ""]

    # Set the color for the emojis
    emoji_color = colors_list['onSurface']

    # Define a font and font size for the emojis (larger size)
    font = ImageFont.truetype("/usr/share/fonts/TTF/SymbolsNerdFont-Regular.ttf", 64)

    num_cols = 10  # Number of columns
    num_rows = 7   # Number of rows
    emoji_size = 64

    # Calculate the spacing between emojis to distribute them evenly
    x_spacing = (width - (num_cols * emoji_size)) // (num_cols + 1)
    y_spacing = (height - (num_rows * emoji_size)) // (num_rows + 1)

    # Create a list to store the previously used emojis
    prev_emoji = []

    # Distribute emojis evenly on the image in a mosaic pattern
    for row in range(num_rows):
        for col in range(num_cols):
            # Choose a random emoji that is not the same as the previous one
            emoji = random.choice([e for e in emojis if e not in prev_emoji])
            
            # Add the chosen emoji to the list of previously used emojis
            prev_emoji.append(emoji)
            
            # Reset the list of previously used emojis if all emojis have been used
            if len(prev_emoji) == len(emojis):
                prev_emoji = []

            x = col * (emoji_size + x_spacing) + x_spacing
            y = row * (emoji_size + y_spacing) + y_spacing

            draw.text((x, y), emoji, fill=emoji_color, font=font)

    image.save(f"{SCRIPTS_DIR}/colors/wall.png")

def read_current_config():
    empty = {"scheme": "dark", "type": "image", "base_color": "0"}
    try:
        with open(CONFIG_FILE, "r") as config:
            return json.load(config)
    except FileNotFoundError:
        with open(CONFIG_FILE, "w") as config:
            json.dump(empty, config)
        return empty
    
def write_current_config(data):
    output_json = json.dumps(data, indent=2)
    with open(CONFIG_FILE, "w") as config:
        config.write(output_json)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if "-i" in sys.argv:
            image = sys.argv[sys.argv.index('-i') + 1]
            scheme = read_current_config()['scheme']

            render_templates(get_colors_from_img(image, scheme))
            write_current_config({"scheme": scheme, "type": "image", "base_color": "0"})
            setup(image)

        elif "--toggle" in sys.argv:
            config = read_current_config()
            scheme = "dark"
            match config['scheme']:
                case "dark":
                    scheme = "light"
                case "light":
                    scheme = "dark"

            match config['type']:
                case "image":
                    image = f"{SCRIPTS_DIR}/colors/wall.png"
                    colors_list = get_colors_from_img(image, scheme)
                    render_templates(colors_list)
                    write_current_config({"scheme": scheme, "type": "image", "base_color": "0"})
                case "emoji":
                    colors_list = get_colors_from_color(config['base_color'], scheme)
                    emoji_wallpaper(colors_list)
                    render_templates(colors_list)
                    write_current_config({"scheme": scheme, "type": "emoji", "base_color": config['base_color']})
                    image = f"{SCRIPTS_DIR}/colors/wall.png"
            setup(image)

        elif "--emoji" in sys.argv:
            color = sys.argv[2]
            scheme = read_current_config()['scheme']
            colors_list = get_colors_from_color(color, scheme)
            emoji_wallpaper(colors_list)
            render_templates(colors_list)
            write_current_config({"scheme": scheme, "type": "emoji", "base_color": color})
            setup(f"{SCRIPTS_DIR}/colors/wall.png")


        elif "--current-scheme" in sys.argv:
            config = read_current_config()
            sys.stdout.write(config['scheme'] + "\n")
            sys.stdout.flush()
        else:
            print(f"unknown parameter: {sys.argv[1]}")

    else:
        print("No summary specifed, try -i 'path/to/img'")