from ignis.widgets import Widget
from .wifi import wifi_control
from .record import record_control
from .dnd import dnd_button
from .dark_mode import dark_mode_button
from .ethernet import ethernet_control
from .vpn import vpn_control
from .qs_button import QSButton
from ignis.services.network import NetworkService

network = NetworkService.get_default()


def add_button(main_box: Widget.Box, buttons: tuple[QSButton, ...], i: int) -> None:
    row = Widget.Box(homogeneous=True)
    if len(main_box.child) > 0:
        row.style = "margin-top: 0.5rem;"

    main_box.append(row)

    button1 = buttons[i]
    row.append(button1)

    if button1.content:
        main_box.append(button1.content)

    if i + 1 < len(buttons):
        button2 = buttons[i + 1]
        button2.style = "margin-left: 0.5rem;"
        row.append(button2)

        if button2.content:
            main_box.append(button2.content)


def qs_fabric(main_box: Widget.Box, *buttons: QSButton) -> None:
    for i in range(0, len(buttons), 2):
        add_button(main_box, buttons, i)


def qs_config(main_box: Widget.Box) -> None:
    qs_fabric(
        main_box,
        *wifi_control(),
        *ethernet_control(),
        *vpn_control(),
        dnd_button(),
        dark_mode_button(),
        record_control(),
    )


def update_box(main_box: Widget.Box):
    main_box.child = []
    qs_config(main_box)


def quick_settings() -> Widget.Box:
    main_box = Widget.Box(vertical=True, css_classes=["qs-main-box"])
    network.wifi.connect("notify::devices", lambda x, y: update_box(main_box))
    network.ethernet.connect("notify::devices", lambda x, y: update_box(main_box))
    network.vpn.connect("notify::connections", lambda x, y: update_box(main_box))

    return main_box
