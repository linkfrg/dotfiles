from ignis.widgets import Widget
from .row import SettingsRow
from typing import Callable
from ignis.gobject import Binding


class SwitchRow(SettingsRow):
    def __init__(
        self,
        active: bool | Binding = False,
        on_change: Callable | None = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self._switch = Widget.Switch(
            active=active,
            on_change=on_change,
            halign="end",
            valign="center",
            hexpand=True,
        )
        self.on_activate = lambda x: self._switch.emit(
            "activate"
        )  # if set "active" property animation will not work
        self.child.append(self._switch)
