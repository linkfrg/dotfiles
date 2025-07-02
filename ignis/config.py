import os
from ignis import utils
from ignis.app import IgnisApp
from ignis.services.wallpaper import WallpaperService
from modules import (
    Bar,
    ControlCenter,
    Launcher,
    NotificationPopup,
    OSD,
    Powermenu,
    Settings,
)
from ignis.css_manager import CssManager, CssInfoPath
from user_options import user_options

app = IgnisApp.get_default()
css_manager = CssManager.get_default()
WallpaperService.get_default()


def format_scss_var(name: str, val: str) -> str:
    return f"${name}: {val};\n"


def patch_style_scss(path: str) -> str:
    with open(path) as file:
        contents = file.read()

    scss_colors = ""

    for key, value in user_options.material.colors.items():
        scss_colors += format_scss_var(key, value)

    string = (
        format_scss_var("darkmode", str(user_options.material.dark_mode).lower())
        + scss_colors
        + contents
    )

    return utils.sass_compile(
        string=string, extra_args=["--load-path", utils.get_current_dir()]
    )


app.add_icons(f"{utils.get_current_dir()}/icons")

css_manager.apply_css(
    CssInfoPath(
        name="main",
        path=os.path.join(utils.get_current_dir(), "style.scss"),
        compiler_function=patch_style_scss,
    )
)

utils.exec_sh("gsettings set org.gnome.desktop.interface gtk-theme Material")
utils.exec_sh("gsettings set org.gnome.desktop.interface icon-theme Papirus")
utils.exec_sh(
    'gsettings set org.gnome.desktop.interface font-name "JetBrains Mono Regular 11"'
)
utils.exec_sh("hyprctl reload")


ControlCenter()

for monitor in range(utils.get_n_monitors()):
    Bar(monitor)

for monitor in range(utils.get_n_monitors()):
    NotificationPopup(monitor)

Launcher()
Powermenu()
OSD()

Settings()
