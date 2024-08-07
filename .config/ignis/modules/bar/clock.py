import datetime
from ignis.widgets import Widget
from ignis.app import app
from ignis.utils import Utils
from .indicator import status_icons
from ignis.services import Service

options = Service.get("options")

def clock(monitor):
    window = app.get_window("ignis_CONTROL_CENTER")
    def on_click(x):
        if window.monitor == monitor:
            window.visible = not window.visible
        else:
            window.set_monitor(monitor)
            window.show()

    return Widget.Button(
        child=Widget.Box(
            child=[
                status_icons(),
                Widget.Label(
                    label=Utils.Poll(1, lambda: datetime.datetime.now().strftime("%H:%M")).bind("output"),
                )
            ]
        ),
        css_classes=window.bind("visible", lambda value: ["clock", "unset", "active"] if value else ["clock", "unset"]),
        on_click=on_click,
    )
