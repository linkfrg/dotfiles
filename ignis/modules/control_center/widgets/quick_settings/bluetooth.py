from ignis import widgets
from ...qs_button import QSButton
from ...menu import Menu
from ....shared_widgets import ToggleBox
from ignis.services.bluetooth import BluetoothService, BluetoothDevice

bluetooth = BluetoothService.get_default()


class BluetoothDeviceItem(widgets.Button):
    def __init__(self, device: BluetoothDevice):
        super().__init__(
            css_classes=["network-item", "unset"],
            on_click=lambda x: device.disconnect_from()
            if device.connected
            else device.connect_to(),
            child=widgets.Box(
                child=[
                    widgets.Icon(
                        image=device.bind("icon_name"),
                    ),
                    widgets.Label(
                        label=device.alias,
                        halign="start",
                        css_classes=["wifi-network-label"],
                    ),
                    widgets.Icon(
                        image="object-select-symbolic",
                        halign="end",
                        hexpand=True,
                        visible=device.bind("connected"),
                    ),
                ]
            ),
        )


class BluetoothMenu(Menu):
    def __init__(self):
        super().__init__(
            name="bluetooth",
            child=[
                ToggleBox(
                    label="Bluetooth",
                    active=bluetooth.powered,
                    on_change=lambda x, state: bluetooth.set_powered(state),
                    css_classes=["network-header-box"],
                ),
                widgets.Box(
                    vertical=True,
                    child=bluetooth.bind(
                        "devices",
                        transform=lambda value: [BluetoothDeviceItem(i) for i in value],
                    ),
                ),
            ],
        )


class BluetoothButton(QSButton):
    def __init__(self):
        menu = BluetoothMenu()

        def get_label(devices: list[BluetoothDevice]) -> str:
            if len(devices) == 0:
                return "Bluetooth"
            elif len(devices) == 1:
                return devices[0].alias
            else:
                return f"{len(devices)} pairs"

        def toggle_menu(x) -> None:
            bluetooth.set_setup_mode(True)
            menu.toggle()

        super().__init__(
            label=bluetooth.bind("connected_devices", get_label),
            icon_name="bluetooth-active-symbolic",
            on_activate=toggle_menu,
            on_deactivate=toggle_menu,
            active=bluetooth.bind("powered"),
            menu=menu,
        )


def bluetooth_control() -> list[QSButton]:
    return [] if bluetooth.state == "absent" else [BluetoothButton()]
