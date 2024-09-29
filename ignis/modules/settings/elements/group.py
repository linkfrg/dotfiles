from typing import List
from ignis.widgets import Widget
from .row import SettingsRow
from ignis.base_widget import BaseWidget


class SettingsGroup(Widget.Box):
    def __init__(
        self, name: str | None, rows: List[SettingsRow | BaseWidget] = [], **kwargs
    ):
        super().__init__(
            vertical=True,
            css_classes=["settings-group"],
            child=[
                Widget.Label(
                    label=name,
                    css_classes=["settings-group-name"],
                    halign="start",
                    visible=True if name else False,
                ),
                Widget.ListBox(rows=[*rows]),
            ],
            **kwargs,
        )
