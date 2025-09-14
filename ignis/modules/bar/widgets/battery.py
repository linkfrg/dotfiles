from ignis import widgets
from ignis.services.upower import UPowerService, UPowerDevice

upower = UPowerService.get_default()


class BatteryItem(widgets.Box):
    def __init__(self, device: UPowerDevice):
        super().__init__(
            css_classes=["battery-item"],
            setup=lambda self: device.connect("removed", lambda x: self.unparent()),
            child=[
                widgets.Icon(
                    icon_name=device.bind("icon_name"), css_classes=["battery-icon"]
                ),
                widgets.Label(
                    label=device.bind("percent", lambda x: f"{int(x)}%"),
                    css_classes=["battery-percent"],
                ),
            ],
        )


class Battery(widgets.Box):
    def __init__(self):
        super().__init__(
            setup=lambda self: upower.connect(
                "battery-added", lambda x, device: self.append(BatteryItem(device))
            ),
        )
