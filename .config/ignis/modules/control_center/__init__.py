from ignis.widgets import Widget
from ignis.app import app
from .volume import volume_control
from .quick_settings import quick_settings
from .user import user
from .media import media


def control_center() -> Widget.Window:
    return Widget.Window(
        visible=False,
        popup=True,
        kb_mode="on_demand",
        layer="top",
        css_classes=["unset"],
        anchor=["top", "right", "bottom", "left"],
        namespace="ignis_CONTROL_CENTER",
        child=Widget.Overlay(
            child=Widget.Button(
                vexpand=True,
                hexpand=True,
                css_classes=["unset"],
                on_click=lambda x: app.close_window("ignis_CONTROL_CENTER"),
            ),
            overlays=[
                Widget.Box(
                    vertical=True,
                    valign="start",
                    halign="end",
                    child=[
                        Widget.Box(
                            vertical=True,
                            css_classes=["control-center"],
                            child=[quick_settings(), volume_control(), user()],
                        ),
                        media(),
                    ],
                )
            ],
        ),
    )
