import re
from ignis.widgets import Widget
from ignis.app import IgnisApp
from ignis.services.applications import (
    ApplicationsService,
    Application,
    ApplicationAction,
)
from ignis.utils import Utils
from gi.repository import Gio  # type: ignore

app = IgnisApp.get_default()

applications = ApplicationsService.get_default()


def is_url(url: str) -> bool:
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain
        r"localhost|"  # localhost
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"  # or ipv4
        r"\[?[A-F0-9]*:[A-F0-9:]+\]?)"  # or ipv6
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    return re.match(regex, url) is not None


class LauncherAppItem(Widget.Button):
    def __init__(self, application: Application) -> None:
        self._application = application
        super().__init__(
            on_click=lambda x: self.launch(),
            on_right_click=lambda x: self._menu.popup(),
            css_classes=["launcher-app"],
            child=Widget.Box(
                child=[
                    Widget.Icon(image=application.icon, pixel_size=48),
                    Widget.Label(
                        label=application.name,
                        ellipsize="end",
                        max_width_chars=30,
                        css_classes=["launcher-app-label"],
                    ),
                ]
            ),
        )
        self.__sync_menu()
        application.connect("notify::is-pinned", lambda x, y: self.__sync_menu())

    def launch(self) -> None:
        self._application.launch()
        app.close_window("ignis_LAUNCHER")

    def launch_action(self, action: ApplicationAction) -> None:
        action.launch()
        app.close_window("ignis_LAUNCHER")

    def __sync_menu(self) -> None:
        self._menu = Widget.PopoverMenu(
            items=[
                Widget.MenuItem(label="Launch", on_activate=lambda x: self.launch()),
                Widget.Separator(),
            ]
            + [
                Widget.MenuItem(
                    label=i.name,
                    on_activate=lambda x, action=i: self.launch_action(action),
                )
                for i in self._application.actions
            ]
            + [
                Widget.Separator(),
                Widget.MenuItem(
                    label="Pin", on_activate=lambda x: self._application.pin()
                )
                if not self._application.is_pinned
                else Widget.MenuItem(
                    label="Unpin", on_activate=lambda x: self._application.unpin()
                ),
            ]
        )
        self.child.append(self._menu)


class SearchWebButton(Widget.Button):
    def __init__(self, query: str):
        self._query = query
        self._url = ""

        browser_desktop_file = Utils.exec_sh(
            "xdg-settings get default-web-browser"
        ).stdout.replace("\n", "")

        app_info = Gio.DesktopAppInfo.new(desktop_id=browser_desktop_file)

        icon_name = "applications-internet-symbolic"
        if app_info:
            icon_string = app_info.get_string("Icon")
            if icon_string:
                icon_name = icon_string

        if not query.startswith(("http://", "https://")) and "." in query:
            query = "https://" + query

        if is_url(query):
            label = f"Visit {query}"
            self._url = query
        else:
            label = "Search in Google"
            self._url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

        super().__init__(
            on_click=lambda x: self.launch(),
            css_classes=["launcher-app"],
            child=Widget.Box(
                child=[
                    Widget.Icon(image=icon_name, pixel_size=48),
                    Widget.Label(
                        label=label,
                        css_classes=["launcher-app-label"],
                    ),
                ]
            ),
        )

    def launch(self) -> None:
        Utils.exec_sh_async(f"xdg-open {self._url}")
        app.close_window("ignis_LAUNCHER")


def launcher() -> Widget.Window:
    def search(entry: Widget.Entry, app_list: Widget.Box) -> None:
        query = entry.text

        if query == "":
            entry.grab_focus()
            app_list.visible = False
            return

        apps = applications.search(applications.apps, query)
        if apps == []:
            app_list.child = [SearchWebButton(query)]
        else:
            app_list.visible = True
            app_list.child = [LauncherAppItem(i) for i in apps[:5]]

    def on_open(window: Widget.Window, entry: Widget.Entry) -> None:
        if not window.visible:
            return

        entry.text = ""
        entry.grab_focus()

    app_list = Widget.Box(vertical=True, visible=False, style="margin-top: 1rem;")
    entry = Widget.Entry(
        hexpand=True,
        placeholder_text="Search",
        css_classes=["launcher-search"],
        on_change=lambda x: search(x, app_list),
        on_accept=lambda x: app_list.child[0].launch()
        if len(app_list.child) > 0
        else None,
    )

    main_box = Widget.Box(
        vertical=True,
        valign="start",
        halign="center",
        css_classes=["launcher"],
        child=[
            Widget.Box(
                css_classes=["launcher-search-box"],
                child=[
                    Widget.Icon(
                        icon_name="system-search-symbolic",
                        pixel_size=24,
                        style="margin-right: 0.5rem;",
                    ),
                    entry,
                ],
            ),
            app_list,
        ],
    )

    return Widget.Window(
        namespace="ignis_LAUNCHER",
        visible=False,
        popup=True,
        kb_mode="on_demand",
        # exclusivity="ignore",
        css_classes=["unset"],
        setup=lambda self: self.connect(
            "notify::visible", lambda x, y: on_open(self, entry)
        ),
        anchor=["top", "right", "bottom", "left"],
        child=Widget.Overlay(
            child=Widget.Button(
                vexpand=True,
                hexpand=True,
                can_focus=False,
                css_classes=["unset"],
                on_click=lambda x: app.close_window("ignis_LAUNCHER"),
                style="background-color: rgba(0, 0, 0, 0.3);",
            ),
            overlays=[main_box],
        ),
    )
