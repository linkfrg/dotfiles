import os
from ignis.widgets import Widget
from ignis.utils import Utils
from ignis.app import app
from ..settings import settings_window

from ignis.services import Service

fetch = Service.get("fetch")
options = Service.get("options")

def format_uptime(value):
    days, hours, minutes, seconds = value
    if days:
        return f"up {days:02}:{hours:02}:{minutes:02}"
    else:
        return f"up {hours:02}:{minutes:02}"


def user() -> Widget.Box:
    user_image = Widget.Picture(
        image=options.bind_option("user_avatar"),
        width=44,
        height=44,
        content_fit="cover",
        style="border-radius: 10rem;",
    )
    username = Widget.Box(
        child=[
            Widget.Label(
                label=os.getenv("USER"), css_classes=["user-name"], halign="start"
            ),
            Widget.Label(
                label=Utils.Poll(timeout=60, callback=lambda: fetch.uptime).bind(
                    "output", lambda value: format_uptime(value)
                ),
                halign="start",
                css_classes=["user-name-secondary"],
            ),
        ],
        vertical=True,
        css_classes=["user-name-box"],
    )

    settings_button = Widget.Button(
        child=Widget.Icon(image="emblem-system-symbolic", pixel_size=20),
        halign="end",
        hexpand=True,
        css_classes=["user-settings"],
        on_click=lambda x: settings_window(),
    )
    power_button = Widget.Button(
        child=Widget.Icon(image="system-shutdown-symbolic", pixel_size=20),
        halign="end",
        css_classes=["user-power"],
        on_click=lambda x: app.toggle_window("ignis_POWERMENU"),
    )

    return Widget.Box(
        child=[user_image, username, settings_button, power_button],
        css_classes=["user", "rec-unset"],
    )
