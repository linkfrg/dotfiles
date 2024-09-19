from ignis.widgets import Widget
from .page import SettingsPage
from options import SETTINGS_OPT_GROUP

class SettingsEntry(Widget.ListBoxRow):
    def __init__(
        self,
        icon: str,
        label: str,
        active_page,
        page: SettingsPage,
        **kwargs,
    ):
        def callback(x):
            active_page.page = page
            active_page.name = label
            if self in self.parent.rows:
                SETTINGS_OPT_GROUP.set_option("last_page", self.parent.rows.index(self))

        super().__init__(
            child=Widget.Box(
                child=[
                    Widget.Icon(image=icon, pixel_size=20),
                    Widget.Label(label=label, style="margin-left: 0.75rem;"),
                ],
            ),
            css_classes=["settings-sidebar-entry"],
            on_activate=callback,
            **kwargs,
        )
