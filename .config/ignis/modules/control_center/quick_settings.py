from ignis.widgets import Widget
from .network import network_control
from .record import record_control
from .dnd import dnd_button
from .dark_mode import dark_mode_button


def quick_settings() -> Widget.Box:
    network_button, wifi_networks_list = network_control()
    record_button, record_menu = record_control()
    return Widget.Box(
        vertical=True,
        child=[
            Widget.Box(
                child=[network_button, dnd_button(), dark_mode_button(), record_button]
            ),
            wifi_networks_list,
            record_menu,
        ],
    )
