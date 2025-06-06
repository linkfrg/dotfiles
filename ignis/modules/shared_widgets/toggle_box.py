from ignis import widgets
from typing import Callable


class ToggleBox(widgets.Box):
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
                widgets.Label(label=label),
                widgets.Switch(
                    halign="end",
                    hexpand=True,
                    active=active,
                    on_change=on_change,
                ),
            ],
            css_classes=["toggle-box"] + css_classes,
        )
