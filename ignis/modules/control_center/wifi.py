from ignis.widgets import Widget
from ignis.utils import Utils
from .qs_button import QSButton
from ignis.services.network import NetworkService, WifiAccessPoint, WifiDevice
from typing import List

network = NetworkService.get_default()


class WifiNetworkItem(Widget.Button):
    def __init__(self, access_point: WifiAccessPoint):
        super().__init__(
            css_classes=["wifi-network-item", "unset"],
            on_click=lambda x: access_point.connect_to_graphical(),
            child=Widget.Box(
                child=[
                    Widget.Icon(
                        image=access_point.bind(
                            "strength", transform=lambda value: access_point.icon_name
                        ),
                    ),
                    Widget.Label(
                        label=access_point.ssid,
                        halign="start",
                        css_classes=["wifi-network-label"],
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


def wifi_qsbutton(device: WifiDevice) -> QSButton:
    networks_list = Widget.Revealer(
        transition_duration=300,
        transition_type="slide_down",
        child=Widget.Box(
            vertical=True,
            css_classes=["control-center-menu"],
            child=[
                Widget.Box(
                    child=[
                        Widget.Label(label="Wi-Fi", css_classes=["wifi-header-label"]),
                        Widget.Switch(
                            halign="end",
                            hexpand=True,
                            active=network.wifi.enabled,
                            on_change=lambda x, state: network.wifi.set_enabled(state),
                        ),
                    ],
                    css_classes=["toggle-box", "wifi-header-box"],
                ),
                Widget.Box(
                    vertical=True,
                    child=device.bind(
                        "access_points",
                        transform=lambda value: [WifiNetworkItem(i) for i in value],
                    ),
                ),
                Widget.Separator(css_classes=["wifi-network-list-separator"]),
                Widget.Button(
                    css_classes=["wifi-network-item", "unset"],
                    on_click=lambda x: Utils.exec_sh_async("nm-connection-editor"),
                    style="margin-bottom: 0;",
                    child=Widget.Box(
                        child=[
                            Widget.Icon(image="preferences-system-symbolic"),
                            Widget.Label(
                                label="Network Settings",
                                halign="start",
                                css_classes=["wifi-network-label"],
                            ),
                        ]
                    ),
                ),
            ],
        ),
    )

    def get_label(ssid: str) -> str:
        if ssid:
            return ssid
        else:
            return "Wi-Fi"

    def get_icon(icon_name: str) -> str:
        if device.ap.is_connected:
            return icon_name
        else:
            return "network-wireless-symbolic"

    def toggle_list(x) -> None:
        device.scan()
        networks_list.toggle()

    return QSButton(
        label=device.ap.bind("ssid", get_label),
        icon_name=device.ap.bind("icon-name", get_icon),
        on_activate=toggle_list,
        on_deactivate=toggle_list,
        active=network.wifi.bind("enabled"),
        content=networks_list,
    )


def wifi_control() -> List[QSButton]:
    return [wifi_qsbutton(dev) for dev in network.wifi.devices]
