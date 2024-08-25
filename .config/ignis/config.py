import os
from ignis.utils import Utils

VERSION = Utils.get_ignis_version().replace("dev0", "").split(".")
EXPECT_VERSION = ["0", "1"]

if int(VERSION[0]) < int(EXPECT_VERSION[0]) or int(VERSION[1]) < int(EXPECT_VERSION[1]):
    print(
        f"My dotfiles requires at least Ignis v{'.'.join(EXPECT_VERSION)}, current version: v{'.'.join(VERSION)}"
    )
    exit(1)

from ignis.app import app  # noqa: E402
from ignis.services import Service  # noqa: E402
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
