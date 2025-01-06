from ignis.utils import Utils
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

app.add_icons(f"{Utils.get_current_dir()}/icons")
app.apply_css(Utils.get_current_dir() + "/style.scss")

Utils.exec_sh("gsettings set org.gnome.desktop.interface gtk-theme Material")
Utils.exec_sh("gsettings set org.gnome.desktop.interface icon-theme Papirus")
Utils.exec_sh(
    'gsettings set org.gnome.desktop.interface font-name "JetBrains Mono Regular 11"'
)
Utils.exec_sh("hyprctl reload")


ControlCenter()

for monitor in range(Utils.get_n_monitors()):
    Bar(monitor)

for monitor in range(Utils.get_n_monitors()):
    NotificationPopup(monitor)

Launcher()
Powermenu()
OSD()

Settings()
