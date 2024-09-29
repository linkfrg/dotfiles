#!/usr/bin/python
import os

from jinja2 import Template
from PIL import Image
from materialyoucolor.quantize import QuantizeCelebi
from materialyoucolor.hct import Hct
from materialyoucolor.scheme.scheme_tonal_spot import SchemeTonalSpot
from materialyoucolor.dynamiccolor.material_dynamic_colors import MaterialDynamicColors
from materialyoucolor.score.score import Score

from ignis.utils import Utils
from ignis.app import IgnisApp
from ignis.base_service import BaseService
from ignis.services.wallpaper import CACHE_WALLPAPER_PATH
from gi.repository import GObject  # type: ignore
from ignis.services.wallpaper import WallpaperService
from ignis.services.options import OptionsService

from .constants import MATERIAL_CACHE_DIR, TEMPLATES, SAMPLE_WALL
from .util import rgba_to_hex, calculate_optimal_size

app = IgnisApp.get_default()


class MaterialService(BaseService):
    def __init__(self):
        super().__init__()

        self._wallpaper = WallpaperService.get_default()

        options = OptionsService.get_default()
        opt_group = options.create_group(name="material", exists_ok=True)
        self._dark_mode_opt = opt_group.create_option(
            name="dark_mode", default=True, exists_ok=True
        )
        self._colors_opt = opt_group.create_option(
            name="colors", default={}, exists_ok=True
        )

        if not os.path.exists(CACHE_WALLPAPER_PATH):
            self.__on_colors_not_found()
        if self.colors == {}:
            self.__on_colors_not_found()

    @GObject.Property
    def dark_mode(self) -> bool:
        return self._dark_mode_opt.value

    @dark_mode.setter
    def dark_mode(self, value: bool) -> None:
        self._dark_mode_opt.value = value
        self.generate_colors(CACHE_WALLPAPER_PATH)

    @GObject.Property
    def colors(self) -> dict:
        return self._colors_opt.value

    def __on_colors_not_found(self) -> None:
        self._wallpaper.set_wallpaper(SAMPLE_WALL)
        self.generate_colors(SAMPLE_WALL)
        Utils.exec_sh_async("hyprctl reload")

    def get_colors_from_img(self, path: str, dark_mode: bool) -> dict[str, str]:
        image = Image.open(path)
        wsize, hsize = image.size
        wsize_new, hsize_new = calculate_optimal_size(wsize, hsize, 128)
        if wsize_new < wsize or hsize_new < hsize:
            image = image.resize((wsize_new, hsize_new), Image.Resampling.BICUBIC)  # type: ignore

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
        dark_colors = self.get_colors_from_img(path, True)
        self._colors_opt.value = colors
        self.__render_templates(colors, dark_colors)
        self.__setup(path)

    def __render_templates(self, colors: dict, dark_colors: dict) -> None:
        for template in os.listdir(TEMPLATES):
            self.render_template(
                colors=colors,
                dark_mode=self.dark_mode,
                input_file=f"{TEMPLATES}/{template}",
                output_file=f"{MATERIAL_CACHE_DIR}/{template}",
            )

        for template in os.listdir(TEMPLATES):
            self.render_template(
                colors=dark_colors,
                dark_mode=True,
                input_file=f"{TEMPLATES}/{template}",
                output_file=f"{MATERIAL_CACHE_DIR}/dark_{template}",
            )

    def render_template(
        self,
        colors: dict,
        input_file: str,
        output_file: str,
        dark_mode: bool | None = None,
    ) -> None:
        if dark_mode is None:
            colors["dark_mode"] = str(self.dark_mode).lower()
        else:
            colors["dark_mode"] = str(dark_mode).lower()
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
        self._wallpaper.set_wallpaper(image_path)
        app.reload_css()
        self.__reload_gtk_theme()
