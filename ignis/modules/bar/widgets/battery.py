from ignis.widgets import Widget
from ignis.services.upower import UPowerService, UPowerDevice

upower = UPowerService.get_default()


class BatteryItem(Widget.Box):
    def __init__(self, device: UPowerDevice):
        super().__init__(
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


class Battery(Widget.Box):
    def __init__(self):
        super().__init__(
            setup=lambda self: upower.connect(
                "battery-added", lambda x, device: self.append(BatteryItem(device))
            ),
        )
