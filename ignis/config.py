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

app = IgnisApp.get_default()
css_manager = CssManager.get_default()
WallpaperService.get_default()

app.add_icons(f"{utils.get_current_dir()}/icons")

css_manager.apply_css(
    CssInfoPath(
        name="main",
        path=utils.get_current_dir() + "/style.scss",
        compiler_function=lambda path: utils.sass_compile(path=path),
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
