from ignis.widgets import Widget
from ignis.services.upower import UPowerService, UPowerDevice

upower = UPowerService.get_default()


def battery_item(device: UPowerDevice) -> Widget.Box:
    return Widget.Box(
        css_classes=["battery-item"],
        setup=lambda self: device.connect("removed", lambda x: self.unparent()),
        child=[
            Widget.Icon(
                icon_name=device.bind("icon_name"), css_classes=["battery-icon"]
            ),
            Widget.Label(
                label=device.bind("percent", lambda x: f"{int(x)}%"),
                css_classes=["battery-percent"],
            ),
            Widget.Scale(
                min=0,
                max=100,
                value=device.bind("percent"),
                sensitive=False,
                css_classes=["battery-scale"],
            ),
        ],
    )


def battery_widget() -> Widget.Box:
    return Widget.Box(
        setup=lambda self: upower.connect(
            "battery-added", lambda x, device: self.append(battery_item(device))
        ),
    )
