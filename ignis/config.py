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

app = IgnisApp.get_default()
WallpaperService.get_default()

app.add_icons(f"{utils.get_current_dir()}/icons")
app.apply_css(utils.get_current_dir() + "/style.scss")

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
