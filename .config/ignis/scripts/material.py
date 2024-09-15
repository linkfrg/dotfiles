#!/usr/bin/python
import os
import math
import ignis
from ignis.logging import logger

try:
    from jinja2 import Template
except ImportError:
    logger.critical("Jinja not found! To use my dotfiles, install python-jinja")
    exit(1)

try:
    from PIL import Image
except ImportError:
    logger.critical("Pillow not found! To use my dotfiles, install python-pillow")
    exit(1)

try:
    from materialyoucolor.quantize import QuantizeCelebi
    from materialyoucolor.hct import Hct
    from materialyoucolor.scheme.scheme_tonal_spot import SchemeTonalSpot
    from materialyoucolor.dynamiccolor.material_dynamic_colors import (
        MaterialDynamicColors,
    )
    from materialyoucolor.score.score import Score
except ImportError:
    logger.critical(
        "materialyoucolor not found! To use my dotfiles, install python-materialyoucolor"
    )
    exit(1)

from ignis.utils import Utils
from ignis.app import IgnisApp
from ignis.gobject import IgnisGObject
from ignis.services.wallpaper import CACHE_WALLPAPER_PATH
from gi.repository import GObject  # type: ignore
from ignis.services.wallpaper import WallpaperService
from ignis.services.options import OptionsService

app = IgnisApp.get_default()

wallpaper = WallpaperService.get_default()
options = OptionsService.get_default()

DARK_MODE_OPTION = "dark_mode"
COLORS_OPTION = "colors"

options.create_option(name="colors", default={}, exists_ok=True)
options.create_option(name="dark_mode", default=True, exists_ok=True)

MATERIAL_CACHE_DIR = f"{ignis.CACHE_DIR}/material"

TEMPLATES = os.path.expanduser("~/.config/ignis/scripts/templates")
SAMPLE_WALL = os.path.expanduser("~/.config/ignis/scripts/sample_wall.png")
os.makedirs(MATERIAL_CACHE_DIR, exist_ok=True)

SWAYLOCK_CONFIG_DIR = os.path.expanduser("~/.config/swaylock")
SWAYLOCK_CONFIG = f"{SWAYLOCK_CONFIG_DIR}/config"
os.makedirs(SWAYLOCK_CONFIG_DIR, exist_ok=True)


def rgba_to_hex(rgba: list) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgba)


def calculate_optimal_size(width: int, height: int, bitmap_size: int) -> tuple:
    image_area = width * height
    bitmap_area = bitmap_size**2
    scale = math.sqrt(bitmap_area / image_area) if image_area > bitmap_area else 1
    new_width = round(width * scale)
    new_height = round(height * scale)
    if new_width == 0:
        new_width = 1
    if new_height == 0:
        new_height = 1
    return new_width, new_height


class MaterialService(IgnisGObject):
    def __init__(self):
        super().__init__()
        if not os.path.exists(CACHE_WALLPAPER_PATH):
            self.__on_colors_not_found()
        if self.colors == {}:
            self.__on_colors_not_found()

    @GObject.Property
    def dark_mode(self) -> bool:
        return options.get_option("dark_mode")

    @dark_mode.setter
    def dark_mode(self, value: bool) -> None:
        options.set_option("dark_mode", value)
        self.generate_colors(CACHE_WALLPAPER_PATH)

    @GObject.Property
    def colors(self) -> dict:
        return options.get_option("colors")

    def __on_colors_not_found(self) -> None:
        wallpaper.set_wallpaper(SAMPLE_WALL)
        self.generate_colors(SAMPLE_WALL)
        Utils.exec_sh_async("hyprctl reload")

    def get_colors_from_img(self, path: str, dark_mode: bool) -> dict[str, str]:
        image = Image.open(path)
        wsize, hsize = image.size
        wsize_new, hsize_new = calculate_optimal_size(wsize, hsize, 128)
        if wsize_new < wsize or hsize_new < hsize:
            image = image.resize((wsize_new, hsize_new), Image.Resampling.BICUBIC)

        pixel_len = image.width * image.height
        image_data = image.getdata()
        pixel_array = [image_data[_] for _ in range(0, pixel_len, 1)]

        colors = QuantizeCelebi(pixel_array, 128)
        argb = Score.score(colors)[0]

        hct = Hct.from_int(argb)
        scheme = SchemeTonalSpot(hct, dark_mode, 0.0)

        material_colors = {}
        for color in vars(MaterialDynamicColors).keys():
            color_name = getattr(MaterialDynamicColors, color)
            if hasattr(color_name, "get_hct"):
                rgba = color_name.get_hct(scheme).to_rgba()
                material_colors[color] = rgba_to_hex(rgba)

        return material_colors

    def generate_colors(self, path: str) -> None:
        colors = self.get_colors_from_img(path, self.dark_mode)
        options.set_option("colors", colors)
        self.__render_templates(colors)
        self.__setup(path)

    def __render_templates(self, colors: dict) -> None:
        for template in os.listdir(TEMPLATES):
            self.render_template(
                colors=colors,
                input_file=f"{TEMPLATES}/{template}",
                output_file=f"{MATERIAL_CACHE_DIR}/{template}",
            )

    def render_template(
        self, colors: dict, input_file: str, output_file: str
    ) -> None:
        colors["dark_mode"] = str(self.dark_mode).lower()
        with open(input_file) as file:
            template_rendered = Template(file.read()).render(colors)

        with open(output_file, "w") as file:
            file.write(template_rendered)

    def __reload_gtk_theme(self) -> None:
        THEME_CMD = "gsettings set org.gnome.desktop.interface gtk-theme {}"
        COLOR_SCHEME_CMD = "gsettings set org.gnome.desktop.interface color-scheme {}"
        Utils.exec_sh_async(THEME_CMD.format("Adwaita"))
        Utils.exec_sh_async(THEME_CMD.format("Material"))
        Utils.exec_sh_async(COLOR_SCHEME_CMD.format("default"))
        Utils.exec_sh_async(COLOR_SCHEME_CMD.format("prefer-dark"))
        Utils.exec_sh_async(COLOR_SCHEME_CMD.format("default"))

    def __setup(self, image_path: str) -> None:
        Utils.exec_sh_async("pkill -SIGUSR1 kitty")
        wallpaper.set_wallpaper(image_path)
        app.reload_css()
        self.__reload_gtk_theme()
        self.__symlink_swaylock_config()

    def __symlink_swaylock_config(self) -> None:
        link_name = f"{MATERIAL_CACHE_DIR}/swaylock"
        if not os.path.exists(SWAYLOCK_CONFIG):
            os.symlink(link_name, SWAYLOCK_CONFIG)
            return

        if not os.path.islink(SWAYLOCK_CONFIG):
            os.remove(SWAYLOCK_CONFIG)
            os.symlink(link_name, SWAYLOCK_CONFIG)


material = MaterialService()
