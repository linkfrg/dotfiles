from ignis import widgets
from .row import SettingsRow
from ignis.base_widget import BaseWidget


class SettingsGroup(widgets.Box):
    def __init__(
        self, name: str | None, rows: list[SettingsRow | BaseWidget] = [], **kwargs
    ):
        super().__init__(
            vertical=True,
            css_classes=["settings-group"],
            child=[
                widgets.Label(
                    label=name,
                    css_classes=["settings-group-name"],
                    halign="start",
                    visible=True if name else False,
                ),
                widgets.ListBox(rows=[*rows]),
            ],
            **kwargs,
        )
