from ignis.widgets import Widget
from ignis.services import Service

network = Service.get("network")
notifications = Service.get("notifications")
recorder = Service.get("recorder")
audio = Service.get("audio")

def indicator_icon(**kwargs):
    return Widget.Icon(style="margin-right: 0.5rem;", css_classes=["unset"], **kwargs)

def network_icon():
    return indicator_icon(
        image=network.wifi.ap.bind(
            "icon-name", transform=lambda value: network.wifi.ap.icon_name
        ),
    )


def dnd_icon():
    return indicator_icon(
        image="notification-disabled-symbolic",
        visible=notifications.bind("dnd"),
    )


def recorder_icon():
    icon = indicator_icon(
        image="media-record-symbolic",
        visible=recorder.bind("active"),
    )
    icon.add_css_class("record-indicator")
    return icon


def volume_icon():
    return indicator_icon(
        image=audio.speaker.bind("icon_name"),
    )


def status_icons():
    return Widget.Box(child=[recorder_icon(), network_icon(), volume_icon(), dnd_icon()])
