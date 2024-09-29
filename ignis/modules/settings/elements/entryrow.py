from ignis.widgets import Widget
from .row import SettingsRow
from typing import Callable
from ignis.gobject import Binding


class EntryRow(SettingsRow):
    def __init__(
        self,
        text: str | Binding | None = None,
        on_change: Callable | None = None,
        width: int | None = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self._entry = Widget.Entry(
            on_change=on_change,
            text=text,
            halign="end",
            valign="center",
            width_request=width,
            hexpand=True,
        )
        self.child.append(self._entry)
