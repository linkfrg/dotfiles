from ignis import widgets
from .page import SettingsPage


class SettingsEntry(widgets.ListBoxRow):
    def __init__(
        self,
        icon: str,
        label: str,
        page: SettingsPage,
        **kwargs,
    ):
        from ..active_page import active_page  # avoid a circular import

        super().__init__(
            child=widgets.Box(
                child=[
                    widgets.Icon(image=icon, pixel_size=20),
                    widgets.Label(label=label, style="margin-left: 0.75rem;"),
                ],
            ),
            css_classes=["settings-sidebar-entry"],
            on_activate=lambda x: active_page.set_value(page),
            **kwargs,
        )
