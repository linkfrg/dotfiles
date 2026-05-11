from ignis import widgets
from .widgets import StatusPill, Tray, KeyboardLayout, Battery, Apps, Workspaces


class Bar(widgets.Window):
    __gtype_name__ = "Bar"

    def __init__(self, monitor: int):
        super().__init__(
            anchor=["left", "top", "right"],
            exclusivity="exclusive",
            monitor=monitor,
            namespace=f"ignis_BAR_{monitor}",
            layer="top",
            kb_mode="none",
            child=widgets.CenterBox(
                css_classes=["bar-widget"],
                start_widget=widgets.Box(child=[Workspaces()]),
                center_widget=widgets.Box(child=[Apps()]),
                end_widget=widgets.Box(
                    child=[Tray(), KeyboardLayout(), Battery(), StatusPill(monitor)]
                ),
            ),
            css_classes=["unset"],
        )
