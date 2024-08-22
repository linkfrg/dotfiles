from ignis.widgets import Widget
from ignis.services import Service

network = Service.get("network")
notifications = Service.get("notifications")
recorder = Service.get("recorder")
audio = Service.get("audio")


def indicator_icon(**kwargs):
    return Widget.Icon(style="margin-right: 0.5rem;", css_classes=["unset"], **kwargs)


def wifi_icon():
    return indicator_icon(
        image=network.wifi.bind("icon-name"),
        visible=network.wifi.bind("devices", lambda value: len(value) > 0),
    )


def ethernet_icon():
    return indicator_icon(image=network.ethernet.bind("icon_name"))


def dnd_icon():
    return indicator_icon(
        image="notification-disabled-symbolic",
        visible=notifications.bind("dnd"),
    )


def recorder_icon():
    def check_state(icon: Widget.Icon) -> None:
        if recorder.is_paused:
            icon.remove_css_class("active")
        else:
            icon.add_css_class("active")

    icon = indicator_icon(
        image="media-record-symbolic",
        visible=recorder.bind("active"),
    )

    icon.add_css_class("record-indicator")

    recorder.connect("notify::is-paused", lambda x, y: check_state(icon))

    return icon


def volume_icon():
    return indicator_icon(
        image=audio.speaker.bind("icon_name"),
    )


def status_icons():
    return Widget.Box(
        child=[recorder_icon(), wifi_icon(), ethernet_icon(), volume_icon(), dnd_icon()]
    )
