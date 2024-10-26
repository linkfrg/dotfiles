import datetime
from ignis.widgets import Widget
from ignis.app import IgnisApp
from ignis.utils import Utils
from ignis.variable import Variable
from .indicator import status_icons

app = IgnisApp.get_default()

current_time = Variable(
    value=Utils.Poll(1000, lambda x: datetime.datetime.now().strftime("%H:%M")).bind(
        "output"
    )
)


def clock(monitor):
    window: Widget.Window = app.get_window("ignis_CONTROL_CENTER")  # type: ignore

    def on_click(x):
        if window.monitor == monitor:
            window.visible = not window.visible
        else:
            window.set_monitor(monitor)
            window.visible = True

    return Widget.Button(
        child=Widget.Box(
            child=[
                status_icons(),
                Widget.Label(
                    label=current_time.bind("value"),
                ),
            ]
        ),
        css_classes=window.bind(
            "visible",
            lambda value: ["clock", "unset", "active"] if value else ["clock", "unset"],
        ),
        on_click=on_click,
    )
