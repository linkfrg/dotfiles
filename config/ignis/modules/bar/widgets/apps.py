from ignis import widgets
from ignis.window_manager import WindowManager
from ignis.services.applications import ApplicationsService, Application
from ignis.menu_model import IgnisMenuModel, IgnisMenuItem, IgnisMenuSeparator

applications = ApplicationsService.get_default()
window_manager = WindowManager.get_default()

TERMINAL_FORMAT = "kitty %command%"


class AppItem(widgets.Button):
    def __init__(self, app: Application):
        menu = widgets.PopoverMenu(
            model=IgnisMenuModel(
                IgnisMenuItem(label="Launch", on_activate=lambda x: app.launch()),
                IgnisMenuSeparator(),
                *(
                    IgnisMenuItem(
                        label=i.name, on_activate=lambda x, action=i: action.launch()
                    )
                    for i in app.actions
                ),
                IgnisMenuSeparator(),
                IgnisMenuItem(label="Unpin", on_activate=lambda x: app.unpin()),
            )
        )

        super().__init__(
            child=widgets.Box(child=[widgets.Icon(image=app.icon, pixel_size=32), menu]),
            on_click=lambda x: app.launch(terminal_format=TERMINAL_FORMAT),
            on_right_click=lambda x: menu.popup(),
            css_classes=["pinned-app", "unset"],
        )


class Apps(widgets.Box):
    def __init__(self):
        super().__init__(
            child=applications.bind(
                "pinned",
                transform=lambda value: [AppItem(app) for app in value]
                + [
                    widgets.Button(
                        child=widgets.Icon(image="start-here-symbolic", pixel_size=32),
                        on_click=lambda x: window_manager.toggle_window("ignis_LAUNCHER"),
                        css_classes=["pinned-app", "unset"],
                    )
                ],
            )
        )
