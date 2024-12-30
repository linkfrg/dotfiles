from ignis.widgets import Widget
from ignis.services.network import Ethernet, Wifi


class IndicatorIcon(Widget.Icon):
    def __init__(self, css_classes: list[str] = [], **kwargs):
        super().__init__(
            style="margin-right: 0.5rem;", css_classes=["unset"] + css_classes, **kwargs
        )


class NetworkIndicatorIcon(IndicatorIcon):
    def __init__(
        self, device_type: Ethernet | Wifi, other_device_type: Wifi | Ethernet
    ):
        self._device_type = device_type
        self._other_device_type = other_device_type

        super().__init__(icon_name=device_type.bind("icon-name"))

        for binding in (
            device_type.bind("devices", self.__check_visibility),
            other_device_type.bind("is_connected", self.__check_visibility),
            device_type.bind("is_connected", self.__check_visibility),
        ):
            self.visible = binding  # type: ignore

    def __check_visibility(self, *args) -> bool:
        return len(self._device_type.devices) > 0 and (
            not self._other_device_type.is_connected or self._device_type.is_connected
        )
