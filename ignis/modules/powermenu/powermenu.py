import asyncio
from ignis import widgets
from ignis import utils
from ignis.window_manager import WindowManager
from typing import Callable

window_manager = WindowManager.get_default()

def create_exec_task(cmd: str) -> None:
    asyncio.create_task(utils.exec_sh_async(cmd))

class PowermenuButton(widgets.Box):
    def __init__(self, label: str, icon_name: str, on_click: Callable) -> None:
        super().__init__(
            child=[
                widgets.Button(
                    child=widgets.Icon(image=icon_name, pixel_size=36),
                    on_click=on_click,
                    css_classes=["powermenu-button", "unset"],
                ),
                widgets.Label(label=label, css_classes=["powermenu-button-label"]),
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
        window_manager.close_window("ignis_POWERMENU")
        create_exec_task("systemctl suspend && hyprlock")


class HyprlandExitButton(PowermenuButton):
    def __init__(self):
        super().__init__(
            label="Sign out",
            icon_name="system-log-out-symbolic",
            on_click=lambda *args: create_exec_task("hyprctl dispatch exit 0"),
        )


class Powermenu(widgets.Window):
    def __init__(self):
        main_box = widgets.Box(
            vertical=True,
            valign="center",
            halign="center",
            css_classes=["powermenu"],
            child=[
                widgets.Box(
                    child=[
                        PowerOffButton(),
                        RebootButton(),
                    ]
                ),
                widgets.Box(
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
            child=widgets.Overlay(
                child=widgets.Button(
                    vexpand=True,
                    hexpand=True,
                    can_focus=False,
                    css_classes=["unset", "powermenu-overlay"],
                    on_click=lambda x: window_manager.close_window("ignis_POWERMENU"),
                ),
                overlays=[main_box],
            ),
            css_classes=["unset"],
        )
