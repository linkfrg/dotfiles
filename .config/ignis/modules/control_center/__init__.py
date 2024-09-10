from typing import Any
from ignis.widgets import Widget
from ignis.app import app
from .volume import volume_control
from .quick_settings import quick_settings
from .user import user
from .media import media
from .notification_center import notification_center
from ignis.utils import Utils
from gi.repository import GObject

def control_center_widget() -> Widget.Box:
    return Widget.Box(
        vertical=True,
        css_classes=["control-center"],
        child=[
            Widget.Box(
                vertical=True,
                css_classes=["control-center-widget"],
                child=[quick_settings(), volume_control(), user(), media()],
            ),
            notification_center(),
        ],
    )


class control_center(Widget.Window):
    def __init__(self) -> None:
        self._revealer = Widget.Revealer(transition_type="slide_left", child=control_center_widget(), transition_duration=300, reveal_child=True)
        self._box = Widget.Box(
            child=[
                Widget.Button(
                    vexpand=True,
                    hexpand=True,
                    css_classes=["unset"],
                    on_click=lambda x: app.close_window("ignis_CONTROL_CENTER"),
                ),
                self._revealer,
            ],
        )
        super().__init__(
            visible=False,
            popup=True,
            kb_mode="on_demand",
            layer="top",
            css_classes=["unset"],
            anchor=["top", "right", "bottom", "left"],
            namespace="ignis_CONTROL_CENTER",
            child=self._box,
        )

    def set_property(self, prop_name: str, value: Any) -> None:
        if prop_name == "visible":
            if value:
                super().set_property(prop_name, value)
            else:
                Utils.Timeout(ms=self._revealer.transition_duration, target=lambda asd=super(): asd.set_property(prop_name, value))
            self._revealer.reveal_child = value
            self.notify("visible")
        else:
            super().set_property(prop_name, value)

    @GObject.Property
    def visible(self) -> bool:
        return self._revealer.reveal_child

    @visible.setter
    def visible(self, value: bool) -> None:
        super().set_visible(value)
        # self._revealer.props.reveal_child = value
