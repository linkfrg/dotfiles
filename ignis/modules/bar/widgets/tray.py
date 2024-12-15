from ignis.widgets import Widget
from ignis.services.system_tray import SystemTrayService, SystemTrayItem

system_tray = SystemTrayService.get_default()


class TrayItem(Widget.Button):
    __gtype_name__ = "TrayItem"

    def __init__(self, item: SystemTrayItem):
        if item.menu:
            menu = item.menu.copy()

        super().__init__(
            child=Widget.Box(
                child=[
                    Widget.Icon(image=item.bind("icon"), pixel_size=24),
                    menu,
                ]
            ),
            tooltip_text=item.bind("tooltip"),
            on_click=lambda x: item.activate(),
            setup=lambda self: item.connect("removed", lambda x: self.unparent()),
            on_right_click=lambda x: menu.popup() if menu else None,
            css_classes=["tray-item", "unset"],
        )


class Tray(Widget.Box):
    __gtype_name__ = "Tray"

    def __init__(self):
        super().__init__(
            css_classes=["tray"],
            setup=lambda self: system_tray.connect(
                "added", lambda x, item: self.append(TrayItem(item))
            ),
            spacing=10,
        )
