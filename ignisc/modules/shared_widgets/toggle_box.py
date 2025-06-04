from ignis.widgets import Widget
from typing import Callable


class ToggleBox(Widget.Box):
    def __init__(
        self,
        label: str,
        active: bool,
        on_change: Callable,
        css_classes: list[str] = [],
        **kwargs,
    ):
        super().__init__(
            child=[
                Widget.Label(label=label),
                Widget.Switch(
                    halign="end",
                    hexpand=True,
                    active=active,
                    on_change=on_change,
                ),
            ],
            css_classes=["toggle-box"] + css_classes,
        )
