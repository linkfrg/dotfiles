from ignis.widgets import Widget
from ignis.app import IgnisApp
from ignis.services.applications import ApplicationsService, Application
from ignis.menu_model import IgnisMenuModel, IgnisMenuItem, IgnisMenuSeparator

applications = ApplicationsService.get_default()
app = IgnisApp.get_default()

TERMINAL_FORMAT = "kitty %command%"


class AppItem(Widget.Button):
    def __init__(self, app: Application):
        menu = Widget.PopoverMenu(
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
            child=Widget.Box(child=[Widget.Icon(image=app.icon, pixel_size=32), menu]),
            on_click=lambda x: app.launch(terminal_format=TERMINAL_FORMAT),
            on_right_click=lambda x: menu.popup(),
            css_classes=["pinned-app", "unset"],
        )


class Apps(Widget.Box):
    def __init__(self):
        super().__init__(
            child=applications.bind(
                "pinned",
                transform=lambda value: [AppItem(app) for app in value]
                + [
                    Widget.Button(
                        child=Widget.Icon(image="start-here-symbolic", pixel_size=32),
                        on_click=lambda x: app.toggle_window("ignis_LAUNCHER"),
                        css_classes=["pinned-app", "unset"],
                    )
                ],
            )
        )
