import os
from ignis.app import app
from ignis.services import Service
from ignis.utils import Utils
from modules.control_center import control_center
from modules.bar import bar
from modules.notification_popup import notification_popup
from modules.osd import OSD
from modules.powermenu import powermenu
from modules.launcher import launcher

Utils.exec_sh("gsettings set org.gnome.desktop.interface gtk-theme Material")
Utils.exec_sh("gsettings set org.gnome.desktop.interface icon-theme Papirus")
Utils.exec_sh('gsettings set org.gnome.desktop.interface font-name "JetBrains Mono Regular 11"')

app.apply_css(os.path.expanduser("~/.config/ignis/style.scss"))

options = Service.get("options")
options.create_option(
    "user_avatar",
    default=f"/var/lib/AccountsService/icons/{os.getenv('USER')}",
    exists_ok=True,
)

control_center()
for monitor in range(Utils.get_n_monitors()):
    bar(monitor)
launcher()
for monitor in range(Utils.get_n_monitors()):
    notification_popup(monitor)

powermenu()
OSD()
