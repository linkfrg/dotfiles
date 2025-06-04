import asyncio
from ignis.widgets import Widget
from ignis.utils import Utils
from ...qs_button import QSButton
from ...menu import Menu
from ignis.services.network import NetworkService, VpnConnection


network = NetworkService.get_default()


class VpnNetworkItem(Widget.Button):
    def __init__(self, conn: VpnConnection):
        super().__init__(
            css_classes=["network-item", "unset"],
            on_click=lambda x: asyncio.create_task(conn.toggle_connection()),
            child=Widget.Box(
                child=[
                    Widget.Label(
                        label=conn.name,
                        ellipsize="end",
                        max_width_chars=20,
                        halign="start",
                    ),
                    Widget.Button(
                        child=Widget.Label(
                            label=conn.bind(
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


class VpnMenu(Menu):
    def __init__(self):
        super().__init__(
            name="vpn",
            child=[
                Widget.Box(
                    css_classes=["network-header-box"],
                    child=[
                        Widget.Icon(icon_name="network-vpn-symbolic", pixel_size=28),
                        Widget.Label(
                            label="VPN connections",
                            css_classes=["network-header-label"],
                        ),
                    ],
                ),
                Widget.Box(
                    vertical=True,
                    child=network.vpn.bind(
                        "connections",
                        transform=lambda value: [VpnNetworkItem(i) for i in value],
                    ),
                ),
                Widget.Separator(),
                Widget.Button(
                    css_classes=["network-item", "unset"],
                    on_click=lambda x: asyncio.create_task(Utils.exec_sh_async("nm-connection-editor")),
                    style="margin-bottom: 0;",
                    child=Widget.Box(
                        child=[
                            Widget.Icon(image="preferences-system-symbolic"),
                            Widget.Label(
                                label="Network Manager",
                                halign="start",
                            ),
                        ]
                    ),
                ),
            ],
        )


class VpnButton(QSButton):
    def __init__(self):
        menu = VpnMenu()

        def get_label(id: str) -> str:
            if id:
                return id
            else:
                return "VPN"

        def get_icon(icon_name: str) -> str:
            if network.vpn.is_connected:
                return icon_name
            else:
                return "network-vpn-symbolic"

        super().__init__(
            label=network.vpn.bind("active_vpn_id", get_label),
            icon_name=network.vpn.bind("icon-name", get_icon),
            on_activate=lambda x: menu.toggle(),
            on_deactivate=lambda x: menu.toggle(),
            active=network.vpn.bind("is-connected"),
            menu=menu,
        )


def vpn_control() -> list[QSButton]:
    if len(network.vpn.connections) > 0:
        return [VpnButton()]
    else:
        return []
