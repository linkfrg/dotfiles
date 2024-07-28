from ignis.widgets import Widget
from .row import SettingsRow

class EntryRow(SettingsRow):
    def __init__(
        self,
        text: str = None,
        on_change: callable = None,
        width: int = None,
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
