from ignis.widgets import Widget
from .page import SettingsPage


class SettingsEntry(Widget.ListBoxRow):
    def __init__(
        self,
        icon: str,
        label: str,
        page: SettingsPage,
        **kwargs,
    ):
        from ..active_page import active_page  # avoid a circular import

        super().__init__(
            child=Widget.Box(
                child=[
                    Widget.Icon(image=icon, pixel_size=20),
                    Widget.Label(label=label, style="margin-left: 0.75rem;"),
                ],
            ),
            css_classes=["settings-sidebar-entry"],
            on_activate=lambda x: active_page.set_value(page),
            **kwargs,
        )
