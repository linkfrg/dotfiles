from ignis.widgets import Widget
from typing import List
from .group import SettingsGroup
from ignis.base_widget import BaseWidget


class SettingsPage(Widget.Scroll):
    def __init__(self, name: str, groups: List[SettingsGroup | BaseWidget] = []):
        super().__init__(
            hexpand=True,
            vexpand=True,
            child=Widget.Box(
                vertical=True,
                hexpand=True,
                vexpand=True,
                css_classes=["settings-page"],
                child=[
                    Widget.Label(
                        label=name, css_classes=["settings-page-name"], halign="start"
                    ),
                    *groups,
                ],
            ),
        )
