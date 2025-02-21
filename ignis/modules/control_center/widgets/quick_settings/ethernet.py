import asyncio
from ignis.widgets import Widget
from ignis.utils import Utils
from ...qs_button import QSButton
from ...menu import Menu
from ignis.services.network import NetworkService, EthernetDevice

network = NetworkService.get_default()


class EthernetConnectionItem(Widget.Button):
    def __init__(self, device: EthernetDevice):
        super().__init__(
            css_classes=["network-item", "unset"],
            on_click=lambda x: asyncio.create_task(device.disconnect_from())
            if device.is_connected
            else asyncio.create_task(device.connect_to()),
            child=Widget.Box(
                child=[
                    Widget.Icon(image="network-wired-symbolic"),
                    Widget.Label(
                        label=device.name,
                        ellipsize="end",
                        max_width_chars=20,
                        halign="start",
                    ),
                    Widget.Button(
                        child=Widget.Label(
                            label=device.bind(
                                "is_connected",
                                lambda value: "Disconnect" if value else "Connect",
                            )
                        ),
                        css_classes=["connect-label", "unset"],
                        halign="end",
                        hexpand=True,
                    ),
                ]
            ),
        )


class EthernetMenu(Menu):
    def __init__(self):
        super().__init__(
            name="ethernet",
            child=[
                Widget.Box(
                    css_classes=["network-header-box"],
                    child=[
                        Widget.Icon(icon_name="network-wired-symbolic", pixel_size=28),
                        Widget.Label(
                            label="Wired connections",
                            css_classes=["network-header-label"],
                        ),
                    ],
                ),
                Widget.Box(
                    vertical=True,
                    child=network.ethernet.bind(
                        "devices",
                        lambda value: [EthernetConnectionItem(i) for i in value],
                    ),
                ),
                Widget.Separator(),
                Widget.Button(
                    css_classes=["network-item", "unset"],
                    style="margin-bottom: 0;",
                    on_click=lambda x: asyncio.create_task(Utils.exec_sh_async("nm-connection-editor")),
                    child=Widget.Box(
                        child=[
                            Widget.Icon(image="preferences-system-symbolic"),
                            Widget.Label(
                                label="Network Settings",
                                halign="start",
                            ),
                        ]
                    ),
                ),
            ],
        )


class EthernetButton(QSButton):
    def __init__(self):
        menu = EthernetMenu()

        super().__init__(
            label="Wired",
            icon_name="network-wired-symbolic",
            on_activate=lambda x: menu.toggle(),
            on_deactivate=lambda x: menu.toggle(),
            menu=menu,
            active=network.ethernet.bind("is_connected"),
        )


def ethernet_control() -> list[QSButton]:
    if len(network.ethernet.devices) > 0:
        return [EthernetButton()]
    else:
        return []
