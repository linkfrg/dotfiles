from ignis.widgets import Widget
from .row import SettingsRow
from typing import Callable
from ignis.gobject import Binding


class SpinRow(SettingsRow):
    def __init__(
        self,
        value: int | Binding = 0,
        on_change: Callable | None = None,
        min: int = 0,
        max: int = 100,
        step: int = 1,
        width: int = 0,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self._spin_button = Widget.SpinButton(
            value=value,
            on_change=on_change,
            min=min,
            max=max,
            halign="end",
            valign="center",
            width_request=width,
            hexpand=True,
            step=step,
        )
        self.child.append(self._spin_button)
