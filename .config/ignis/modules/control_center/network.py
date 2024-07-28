from ignis.widgets import Widget
from ignis.utils import Utils
from .qs_button import QSButton
from ignis.services import Service
from ignis.services.network import NetworkService, WifiAccessPoint
from typing import List
from typing import Tuple

network: NetworkService = Service.get("network")


class WifiNetworkItem(Widget.Button):
    def __init__(self, access_point: WifiAccessPoint):
        super().__init__(
            css_classes=["wifi-entry", "unset"],
            on_click=lambda x: access_point.connect_to_graphical(),
            child=Widget.Box(
                child=[
                    Widget.Icon(
                        image=access_point.bind(
                            "strength", transform=lambda value: access_point.icon_name
                        )
                    ),
                    Widget.Label(
                        label=access_point.ssid,
                        halign="start",
                        style="margin-left: 0.35rem;",
                    ),
                    Widget.Icon(
                        image="object-select-symbolic",
                        halign="end",
                        hexpand=True,
                        visible=access_point.bind("is_connected"),
                    ),
                ]
            ),
        )


def network_control() -> Tuple[QSButton, Widget.Revealer]:
    def get_wifi_entries(value: list[WifiAccessPoint]) -> List[WifiNetworkItem]:
        if network.wifi.enabled:
            if value:
                return [WifiNetworkItem(i) for i in value]
            else:
                return [Widget.Label(label="No Wi-Fi networks found.")]
        else:
            return [Widget.Label(label="Wi-Fi is not available.")]

    wifi_networks_list = Widget.Revealer(
        transition_duration=300,
        transition_type="slide_down",
        child=Widget.Box(
            vertical=True,
            css_classes=["wifi-network-list"],
            child=[
                Widget.Box(
                    child=[
                        Widget.Label(label="Wi-Fi", style="font-size: 1.2rem;"),
                        Widget.Switch(
                            halign="end",
                            hexpand=True,
                            active=network.wifi.enabled,
                            on_change=lambda x, state: network.wifi.set_enabled(state),
                        ),
                    ],
                    css_classes=["toggle-box"],
                    style="margin-bottom: 0.5rem;",
                ),
                Widget.Box(
                    vertical=True,
                    child=network.wifi.bind(
                        "access_points", transform=lambda value: get_wifi_entries(value)
                    ),
                ),
                Widget.Separator(),
                Widget.Button(
                    css_classes=["wifi-entry", "unset"],
                    on_click=lambda x: Utils.exec_sh_async("nm-connection-editor"),
                    child=Widget.Box(
                        child=[
                            Widget.Icon(image="preferences-system-symbolic"),
                            Widget.Label(
                                label="Network Settings",
                                halign="start",
                                style="margin-left: 0.25rem;",
                            ),
                        ]
                    ),
                ),
            ],
        ),
    )

    return QSButton(
        icon_name=network.wifi.ap.bind("icon-name"),
        on_activate=lambda x: (network.wifi.scan(), wifi_networks_list.toggle()),
        on_deactivate=lambda x: (network.wifi.scan(), wifi_networks_list.toggle()),
        style="margin-left: 0;",
        active=network.wifi.bind("enabled"),
    ), wifi_networks_list
