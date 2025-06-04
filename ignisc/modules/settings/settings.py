from ignis.widgets import Widget
from ignis.app import IgnisApp
from user_options import user_options
from .active_page import active_page
from .pages import (
    AboutEntry,
    AppearanceEntry,
    NotificationsEntry,
    RecorderEntry,
    UserEntry,
)

app = IgnisApp.get_default()


class Settings(Widget.RegularWindow):
    def __init__(self) -> None:
        content = Widget.Box(
            hexpand=True,
            vexpand=True,
            child=active_page.bind("value", transform=lambda value: [value]),
        )
        self._listbox = Widget.ListBox()

        navigation_sidebar = Widget.Box(
            vertical=True,
            css_classes=["settings-sidebar"],
            child=[
                Widget.Label(
                    label="Settings",
                    halign="start",
                    css_classes=["settings-sidebar-label"],
                ),
                self._listbox,
            ],
        )

        super().__init__(
            default_width=900,
            default_height=600,
            resizable=False,
            hide_on_close=True,
            visible=False,
            child=Widget.Box(child=[navigation_sidebar, content]),
            namespace="ignis_SETTINGS",
        )

        self.connect("notify::visible", self.__on_open)

    def __on_open(self, *args) -> None:
        if self.visible is False:
            return

        if len(self._listbox.rows) != 0:
            return

        rows = [
            NotificationsEntry(),
            RecorderEntry(),
            AppearanceEntry(),
            UserEntry(),
            AboutEntry(),
        ]

        self._listbox.rows = rows
        self._listbox.activate_row(rows[user_options.settings.last_page])

        self._listbox.connect("row-activated", self.__update_last_page)

    def __update_last_page(self, x, row) -> None:
        user_options.settings.last_page = self._listbox.rows.index(row)
