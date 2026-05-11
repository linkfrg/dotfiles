import re
import asyncio
from ignis import widgets
from ignis.window_manager import WindowManager
from ignis.services.applications import (
    ApplicationsService,
    Application,
    ApplicationAction,
)
from ignis import utils
from ignis.menu_model import IgnisMenuModel, IgnisMenuItem, IgnisMenuSeparator
from gi.repository import Gio  # type: ignore

window_manager = WindowManager.get_default()

applications = ApplicationsService.get_default()

TERMINAL_FORMAT = "kitty %command%"


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


class LauncherAppItem(widgets.Button):
    def __init__(self, application: Application) -> None:
        self._menu = widgets.PopoverMenu()

        self._application = application
        super().__init__(
            on_click=lambda x: self.launch(),
            on_right_click=lambda x: self._menu.popup(),
            css_classes=["launcher-app"],
            child=widgets.Box(
                child=[
                    widgets.Icon(image=application.icon, pixel_size=48),
                    widgets.Label(
                        label=application.name,
                        ellipsize="end",
                        max_width_chars=30,
                        css_classes=["launcher-app-label"],
                    ),
                    self._menu,
                ]
            ),
        )
        self.__sync_menu()
        application.connect("notify::is-pinned", lambda x, y: self.__sync_menu())

    def launch(self) -> None:
        self._application.launch(terminal_format=TERMINAL_FORMAT)
        window_manager.close_window("ignis_LAUNCHER")

    def launch_action(self, action: ApplicationAction) -> None:
        action.launch()
        window_manager.close_window("ignis_LAUNCHER")

    def __sync_menu(self) -> None:
        self._menu.model = IgnisMenuModel(
            IgnisMenuItem(label="Launch", on_activate=lambda x: self.launch()),
            IgnisMenuSeparator(),
            *(
                IgnisMenuItem(
                    label=i.name,
                    on_activate=lambda x, action=i: self.launch_action(action),
                )
                for i in self._application.actions
            ),
            IgnisMenuSeparator(),
            IgnisMenuItem(label="Pin", on_activate=lambda x: self._application.pin())
            if not self._application.is_pinned
            else IgnisMenuItem(
                label="Unpin", on_activate=lambda x: self._application.unpin()
            ),
        )


class SearchWebButton(widgets.Button):
    def __init__(self, query: str):
        self._query = query
        self._url = ""

        browser_desktop_file = utils.exec_sh(
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
            child=widgets.Box(
                child=[
                    widgets.Icon(image=icon_name, pixel_size=48),
                    widgets.Label(
                        label=label,
                        css_classes=["launcher-app-label"],
                    ),
                ]
            ),
        )

    def launch(self) -> None:
        asyncio.create_task(utils.exec_sh_async(f"xdg-open {self._url}"))
        window_manager.close_window("ignis_LAUNCHER")


class Launcher(widgets.Window):
    def __init__(self):
        self._app_list = widgets.Box(
            vertical=True, visible=False, style="margin-top: 1rem;"
        )
        self._entry = widgets.Entry(
            hexpand=True,
            placeholder_text="Search",
            css_classes=["launcher-search"],
            on_change=self.__search,
            on_accept=self.__on_accept,
        )

        main_box = widgets.Box(
            vertical=True,
            valign="start",
            halign="center",
            css_classes=["launcher"],
            child=[
                widgets.Box(
                    css_classes=["launcher-search-box"],
                    child=[
                        widgets.Icon(
                            icon_name="system-search-symbolic",
                            pixel_size=24,
                            style="margin-right: 0.5rem;",
                        ),
                        self._entry,
                    ],
                ),
                self._app_list,
            ],
        )

        super().__init__(
            namespace="ignis_LAUNCHER",
            visible=False,
            popup=True,
            kb_mode="on_demand",
            css_classes=["unset"],
            setup=lambda self: self.connect("notify::visible", self.__on_open),
            anchor=["top", "right", "bottom", "left"],
            child=widgets.Overlay(
                child=widgets.Button(
                    vexpand=True,
                    hexpand=True,
                    can_focus=False,
                    css_classes=["unset"],
                    on_click=lambda x: window_manager.close_window("ignis_LAUNCHER"),
                    style="background-color: rgba(0, 0, 0, 0.3);",
                ),
                overlays=[main_box],
            ),
        )

    def __on_open(self, *args) -> None:
        if not self.visible:
            return

        self._entry.text = ""
        self._entry.grab_focus()

    def __on_accept(self, *args) -> None:
        if len(self._app_list.child) > 0:
            self._app_list.child[0].launch()

    def __search(self, *args) -> None:
        query = self._entry.text

        if query == "":
            self._entry.grab_focus()
            self._app_list.visible = False
            return

        apps = applications.search(applications.apps, query)
        if apps == []:
            self._app_list.child = [SearchWebButton(query)]
        else:
            self._app_list.visible = True
            self._app_list.child = [LauncherAppItem(i) for i in apps[:5]]
