from ignis.widgets import Widget
from ignis.gobject import IgnisGObject
from gi.repository import GObject  # type: ignore
from .notifications import notifications_entry
from .about import about_entry
from .appearance import appearance_entry
from .recorder import recorder_entry
from .user import user_entry
from .elements import SettingsPage
from ignis.app import IgnisApp
from ignis.exceptions import WindowNotFoundError
from options import settings_last_page

app = IgnisApp.get_default()


class ActivePage(IgnisGObject):
    def __init__(self, name: str | None, page: SettingsPage | None):
        super().__init__()
        self._name = name
        self._page = page

    @GObject.Property
    def name(self) -> str | None:
        return self._name

    @name.setter
    def name(self, value: str | None) -> None:
        self._name = value

    @GObject.Property
    def page(self) -> SettingsPage | None:
        return self._page

    @page.setter
    def page(self, value: SettingsPage | None) -> None:
        self._page = value


def settings_widget():
    active_page = ActivePage(name="Settings", page=None)
    content = Widget.Box(
        hexpand=True,
        vexpand=True,
        child=active_page.bind("page", transform=lambda value: [value]),
    )
    listbox = Widget.ListBox(
        rows=[
            notifications_entry(active_page),
            recorder_entry(active_page),
            appearance_entry(active_page),
            user_entry(active_page),
            about_entry(active_page),
        ],
    )

    listbox.select_row(listbox.rows[settings_last_page.value])

    navigation_sidebar = Widget.Box(
        vertical=True,
        css_classes=["settings-sidebar"],
        child=[
            Widget.Label(
                label="Settings", halign="start", css_classes=["settings-sidebar-label"]
            ),
            listbox,
        ],
    )

    return Widget.Box(child=[navigation_sidebar, content])


def settings_window():
    try:
        app.get_window("ignis_SETTINGS")
    except WindowNotFoundError:
        return Widget.RegularWindow(
            default_width=900,
            default_height=600,
            resizable=False,
            child=settings_widget(),
            namespace="ignis_SETTINGS",
        )
