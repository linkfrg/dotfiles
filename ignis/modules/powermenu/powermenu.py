import asyncio
from ignis.widgets import Widget
from ignis.utils import Utils
from ignis.app import IgnisApp
from typing import Callable

app = IgnisApp.get_default()

def create_exec_task(cmd: str) -> None:
    asyncio.create_task(Utils.exec_sh_async(cmd))

class PowermenuButton(Widget.Box):
    def __init__(self, label: str, icon_name: str, on_click: Callable) -> None:
        super().__init__(
            child=[
                Widget.Button(
                    child=Widget.Icon(image=icon_name, pixel_size=36),
                    on_click=on_click,
                    css_classes=["powermenu-button", "unset"],
                ),
                Widget.Label(label=label, css_classes=["powermenu-button-label"]),
            ],
            vertical=True,
            css_classes=["powermenu-button-box"],
        )


class PowerOffButton(PowermenuButton):
    def __init__(self):
        super().__init__(
            label="Power off",
            icon_name="system-shutdown-symbolic",
            on_click=lambda *args: create_exec_task("poweroff"),
        )


class RebootButton(PowermenuButton):
    def __init__(self):
        super().__init__(
            label="Reboot",
            icon_name="system-reboot-symbolic",
            on_click=lambda *args: create_exec_task("reboot"),
        )


class SuspendButton(PowermenuButton):
    def __init__(self):
        super().__init__(
            label="Suspend", icon_name="night-light-symbolic", on_click=self.__invoke
        )

    def __invoke(self, *args) -> None:
        app.close_window("ignis_POWERMENU")
        create_exec_task("systemctl suspend && hyprlock")


class HyprlandExitButton(PowermenuButton):
    def __init__(self):
        super().__init__(
            label="Sign out",
            icon_name="system-log-out-symbolic",
            on_click=lambda *args: create_exec_task("hyprctl dispatch exit 0"),
        )


class Powermenu(Widget.Window):
    def __init__(self):
        main_box = Widget.Box(
            vertical=True,
            valign="center",
            halign="center",
            css_classes=["powermenu"],
            child=[
                Widget.Box(
                    child=[
                        PowerOffButton(),
                        RebootButton(),
                    ]
                ),
                Widget.Box(
                    child=[
                        SuspendButton(),
                        HyprlandExitButton(),
                    ]
                ),
            ],
        )
        super().__init__(
            popup=True,
            kb_mode="on_demand",
            namespace="ignis_POWERMENU",
            exclusivity="ignore",
            anchor=["left", "right", "top", "bottom"],
            visible=False,
            child=Widget.Overlay(
                child=Widget.Button(
                    vexpand=True,
                    hexpand=True,
                    can_focus=False,
                    css_classes=["unset", "powermenu-overlay"],
                    on_click=lambda x: app.close_window("ignis_POWERMENU"),
                ),
                overlays=[main_box],
            ),
            css_classes=["unset"],
        )
