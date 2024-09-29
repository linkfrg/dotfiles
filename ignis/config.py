from check_version import check_version

check_version()

from ignis.utils import Utils  # noqa: E402
from ignis.app import IgnisApp  # noqa: E402
from modules.control_center import control_center  # noqa: E402
from modules.bar import bar  # noqa: E402
from modules.notification_popup import notification_popup  # noqa: E402
from modules.osd import OSD  # noqa: E402
from modules.powermenu import powermenu  # noqa: E402
from modules.launcher import launcher  # noqa: E402

Utils.exec_sh("gsettings set org.gnome.desktop.interface gtk-theme Material")
Utils.exec_sh("gsettings set org.gnome.desktop.interface icon-theme Papirus")
Utils.exec_sh(
    'gsettings set org.gnome.desktop.interface font-name "JetBrains Mono Regular 11"'
)
Utils.exec_sh("hyprctl reload")
app = IgnisApp.get_default()
app.apply_css(Utils.get_current_dir() + "/style.scss")


control_center()
for monitor in range(Utils.get_n_monitors()):
    bar(monitor)
launcher()
for monitor in range(Utils.get_n_monitors()):
    notification_popup(monitor)

powermenu()
OSD()
