from ignis.widgets import Widget
from ignis.app import IgnisApp
from ignis.services.applications import ApplicationsService

applications = ApplicationsService.get_default()
app = IgnisApp.get_default()


class AppItem(Widget.Button):
    def __init__(self, app):
        menu = Widget.PopoverMenu(
            items=[
                Widget.MenuItem(label="Launch", on_activate=lambda x: app.launch()),
                Widget.Separator(),
            ]
            + [
                Widget.MenuItem(
                    label=i.name, on_activate=lambda x, action=i: action.launch()
                )
                for i in app.actions
            ]
            + [
                Widget.Separator(),
                Widget.MenuItem(label="Unpin", on_activate=lambda x: app.unpin()),
            ]
        )

        super().__init__(
            child=Widget.Box(child=[Widget.Icon(image=app.icon, pixel_size=32), menu]),
            on_click=lambda x: app.launch(),
            on_right_click=lambda x: menu.popup(),
            css_classes=["pinned-app", "unset"],
        )


def launcher_button():
    return Widget.Button(
        child=Widget.Icon(image="start-here-symbolic", pixel_size=32),
        on_click=lambda x: app.toggle_window("ignis_LAUNCHER"),
        css_classes=["pinned-app", "unset"],
    )


def pinned_apps():
    return Widget.Box(
        child=applications.bind(
            "pinned",
            transform=lambda value: [AppItem(app) for app in value]
            + [launcher_button()],
        )
    )
