from ignis.widgets import Widget
from ignis.utils import Utils
from .qs_button import QSButton
from typing import List
from ignis.services.network import NetworkService, VpnConnection


network = NetworkService.get_default()


class VpnNetworkItem(Widget.Button):
    def __init__(self, conn: VpnConnection):

        super().__init__(
            css_classes=["vpn-connection-item", "unset"],
            on_click=lambda x: conn.toggle_connection(),
            child=Widget.Box(
                child=[
                    Widget.Label(
                        label=conn.name,
                        ellipsize="end",
                        max_width_chars=20,
                        halign="start",
                        css_classes=["vpn-connection-label"],
                    ),
                    Widget.Button(
                        child=Widget.Label(
                            label=conn.bind(
                                "is_connected",
                                lambda value: "Disconnect" if value else "Connect",
                            )
                        ),
                        css_classes=["vpn-connection-item-connect-label", "unset"],
                        halign="end",
                        hexpand=True,
                    ),
                ]
            ),
        )


def vpn_qsbutton() -> QSButton:
    networks_list = Widget.Revealer(
        transition_duration=300,
        transition_type="slide_down",
        child=Widget.Box(
            vertical=True,
            css_classes=["control-center-menu"],
            child=[
                Widget.Box(
                    css_classes=["vpn-header-box"],
                    child=[
                        Widget.Icon(
                            icon_name="network-vpn-symbolic", pixel_size=28),
                        Widget.Label(
                            label="VPN connections",
                            css_classes=["vpn-header-label"],
                        ),
                    ],
                ),
                Widget.Box(
                    vertical=True,
                    child=network.vpn.bind(
                        "connections",
                        transform=lambda value: [
                            VpnNetworkItem(i) for i in value],
                    ),
                ),
                Widget.Separator(
                    css_classes=["vpn-connection-list-separator"]),
                Widget.Button(
                    css_classes=["vpn-connection-item", "unset"],
                    on_click=lambda x: Utils.exec_sh_async(
                        "nm-connection-editor"),
                    style="margin-bottom: 0;",
                    child=Widget.Box(
                        child=[
                            Widget.Icon(image="preferences-system-symbolic"),
                            Widget.Label(
                                label="Network Manager",
                                halign="start",
                                css_classes=["vpn-connection-label"],
                            ),
                        ]
                    ),
                ),
            ],
        ),
    )

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

    def toggle_list(x) -> None:
        networks_list.toggle()

    return QSButton(
        label=network.vpn.bind("active_vpn_id", get_label),
        icon_name=network.vpn.bind("icon-name", get_icon),
        on_activate=toggle_list,
        on_deactivate=toggle_list,
        active=network.vpn.bind("is-connected"),
        content=networks_list,
    )


def vpn_control() -> List[QSButton]:
    if len(network.vpn.connections) > 0:
        return [vpn_qsbutton()]
    else:
        return []
