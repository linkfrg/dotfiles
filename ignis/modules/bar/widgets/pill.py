import datetime
from ignis.widgets import Widget
from ignis.app import IgnisApp
from ignis.utils import Utils
from ignis.variable import Variable
from ignis.services.network import NetworkService
from ignis.services.notifications import NotificationService
from ignis.services.recorder import RecorderService
from ignis.services.audio import AudioService
from ..indicator_icon import IndicatorIcon, NetworkIndicatorIcon
from ignis.options import options

network = NetworkService.get_default()
notifications = NotificationService.get_default()
recorder = RecorderService.get_default()
audio = AudioService.get_default()

app = IgnisApp.get_default()

current_time = Variable(
    value=Utils.Poll(1000, lambda x: datetime.datetime.now().strftime("%H:%M")).bind(
        "output"
    )
)


class WifiIcon(NetworkIndicatorIcon):
    def __init__(self):
        super().__init__(device_type=network.wifi, other_device_type=network.ethernet)


class EthernetIcon(NetworkIndicatorIcon):
    def __init__(self):
        super().__init__(device_type=network.ethernet, other_device_type=network.wifi)


class VpnIcon(IndicatorIcon):
    def __init__(self):
        super().__init__(
            image=network.vpn.bind("icon_name"),
            visible=network.vpn.bind("is_connected"),
        )


class DNDIcon(IndicatorIcon):
    def __init__(self):
        super().__init__(
            image="notification-disabled-symbolic",
            visible=options.notifications.bind("dnd"),
        )


class RecorderIcon(IndicatorIcon):
    def __init__(self):
        super().__init__(
            image="media-record-symbolic",
            css_classes=["record-indicator"],
            setup=lambda self: recorder.connect(
                "notify::is-paused", self.__update_css_class
            ),
            visible=recorder.bind("active"),
        )

    def __update_css_class(self, *args) -> None:
        if recorder.is_paused:
            self.remove_css_class("active")
        else:
            self.add_css_class("active")


class VolumeIcon(IndicatorIcon):
    def __init__(self):
        super().__init__(
            image=audio.speaker.bind("icon_name"),
        )


class StatusPill(Widget.Button):
    def __init__(self, monitor: int):
        self._monitor = monitor
        self._window: Widget.Window = app.get_window("ignis_CONTROL_CENTER")  # type: ignore

        super().__init__(
            child=Widget.Box(
                child=[
                    RecorderIcon(),
                    WifiIcon(),
                    EthernetIcon(),
                    VpnIcon(),
                    VolumeIcon(),
                    DNDIcon(),
                    Widget.Label(
                        label=current_time.bind("value"),
                    ),
                ]
            ),
            css_classes=self._window.bind(
                "visible",
                lambda value: ["clock", "unset", "active"]
                if value
                else ["clock", "unset"],
            ),
            on_click=self.__on_click,
        )

    def __on_click(self, x) -> None:
        if self._window.monitor == self._monitor:
            self._window.visible = not self._window.visible
        else:
            self._window.set_monitor(self._monitor)
            self._window.visible = True
