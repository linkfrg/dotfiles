from ignis.utils import Utils
from ignis.app import IgnisApp
from modules.control_center import control_center
from modules.bar import bar
from modules.notification_popup import notification_popup
from modules.osd import OSD
from modules.powermenu import powermenu
from modules.launcher import launcher

app = IgnisApp.get_default()

app.add_icons(f"{Utils.get_current_dir()}/icons")
app.apply_css(Utils.get_current_dir() + "/style.scss")

Utils.exec_sh("gsettings set org.gnome.desktop.interface gtk-theme Material")
Utils.exec_sh("gsettings set org.gnome.desktop.interface icon-theme Papirus")
Utils.exec_sh(
    'gsettings set org.gnome.desktop.interface font-name "JetBrains Mono Regular 11"'
)
Utils.exec_sh("hyprctl reload")


control_center()
for monitor in range(Utils.get_n_monitors()):
    bar(monitor)
launcher()
for monitor in range(Utils.get_n_monitors()):
    notification_popup(monitor)

powermenu()
OSD()
