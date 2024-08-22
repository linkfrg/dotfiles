import os
import datetime
from ignis.widgets import Widget
from ignis.utils import Utils
from ignis.services import Service

options = Service.get("options")


def date() -> Widget.Label:
    return Widget.Label(
        label=Utils.Poll(
            1, lambda x: datetime.datetime.now().strftime("%a, %b %d")
        ).bind("output"),
        css_classes=["header-date"],
        halign="start",
    )


def clock() -> Widget.Label:
    return Widget.Label(
        label=Utils.Poll(1, lambda x: datetime.datetime.now().strftime("%H:%M")).bind(
            "output"
        ),
        css_classes=["header-clock"],
    )


def user_image() -> Widget.Picture:
    return Widget.Box(
        child=[
            Widget.Picture(
                image=options.bind_option(
                    "user_avatar",
                    lambda value: "user-info" if not os.path.exists(value) else value,
                ),
                width=52,
                height=52,
                content_fit="cover",
                style="border-radius: 10rem;",
            )
        ],
        halign="end",
        valign="start",
        hexpand=True,
    )


def username() -> Widget.Label:
    return Widget.Label(
        label=os.getenv("USER"), css_classes=["user-name"], halign="start"
    )


def header() -> Widget.Box:
    return Widget.Box(
        child=[
            Widget.Box(vertical=True, child=[clock(), date()]),
            user_image(),
        ]
    )
