from ignis import widgets
from .group import SettingsGroup
from ignis.base_widget import BaseWidget


class SettingsPage(widgets.Scroll):
    def __init__(self, name: str, groups: list[SettingsGroup | BaseWidget] = []):
        super().__init__(
            hexpand=True,
            vexpand=True,
            child=widgets.Box(
                vertical=True,
                hexpand=True,
                vexpand=True,
                css_classes=["settings-page"],
                child=[
                    widgets.Label(
                        label=name, css_classes=["settings-page-name"], halign="start"
                    ),
                    *groups,
                ],
            ),
        )
