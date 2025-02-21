import asyncio
from ignis.widgets import Widget
from ignis.utils import Utils
from ignis.services.audio import AudioService, Stream
from typing import Literal
from ..menu import Menu
from ...shared_widgets import MaterialVolumeSlider

audio = AudioService.get_default()

AUDIO_TYPES = {
    "speaker": {"menu_icon": "audio-headphones-symbolic", "menu_label": "Sound Output"},
    "microphone": {
        "menu_icon": "microphone-sensitivity-high-symbolic",
        "menu_label": "Sound Input",
    },
}


class DeviceItem(Widget.Button):
    def __init__(self, stream: Stream, _type: Literal["speaker", "microphone"]):
        super().__init__(
            child=Widget.Box(
                child=[
                    Widget.Icon(image="audio-card-symbolic"),
                    Widget.Label(
                        label=stream.description,
                        ellipsize="end",
                        max_width_chars=30,
                        halign="start",
                        css_classes=["volume-entry-label"],
                    ),
                    Widget.Icon(
                        image="object-select-symbolic",
                        halign="end",
                        hexpand=True,
                        visible=stream.bind("is_default"),
                    ),
                ]
            ),
            css_classes=["volume-entry", "unset"],
            hexpand=True,
            setup=lambda self: stream.connect("removed", lambda x: self.unparent()),
            on_click=lambda x: setattr(audio, _type, stream),
        )


class DeviceMenu(Menu):
    def __init__(self, _type: Literal["speaker", "microphone"], style: str = ""):
        data = AUDIO_TYPES[_type]

        super().__init__(
            name=f"volume-{_type}",
            child=[
                Widget.Box(
                    child=[
                        Widget.Icon(image=data["menu_icon"], pixel_size=24),
                        Widget.Label(
                            label=data["menu_label"],
                            halign="start",
                            css_classes=["volume-entry-list-header-label"],
                        ),
                    ],
                    css_classes=["volume-entry-list-header-box"],
                ),
                Widget.Box(
                    vertical=True,
                    setup=lambda self: audio.connect(
                        f"{_type}-added",
                        lambda x, stream: self.append(DeviceItem(stream, _type)),
                    ),
                ),
                Widget.Separator(css_classes=["volume-entry-list-separator"]),
                Widget.Button(
                    child=Widget.Box(
                        child=[
                            Widget.Icon(image="preferences-system-symbolic"),
                            Widget.Label(
                                label="Sound Settings",
                                halign="start",
                                css_classes=["volume-entry-label"],
                            ),
                        ]
                    ),
                    css_classes=["volume-entry", "unset"],
                    style="margin-bottom: 0;",
                    on_click=lambda x: asyncio.create_task(Utils.exec_sh_async("pavucontrol")),
                ),
            ],
        )

        self.box.add_css_class(f"volume-menubox-{_type}")


class VolumeSlider(Widget.Box):
    def __init__(self, _type: Literal["speaker", "microphone"]):
        stream = getattr(audio, _type)

        icon = Widget.Button(
            child=Widget.Icon(
                image=stream.bind("icon_name"),
                pixel_size=18,
            ),
            css_classes=["material-slider-icon", "unset", "hover-surface"],
            on_click=lambda x: stream.set_is_muted(not stream.is_muted),
        )

        device_menu = DeviceMenu(_type=_type)

        scale = MaterialVolumeSlider(
            stream=stream,
            on_change=lambda x: stream.set_volume(x.value),
            sensitive=stream.bind("is_muted", lambda value: not value),
        )

        arrow = Widget.Button(
            child=Widget.Arrow(pixel_size=20, rotated=device_menu.bind("reveal_child")),
            css_classes=["material-slider-arrow", "hover-surface"],
            on_click=lambda x: device_menu.toggle(),
        )
        super().__init__(
            vertical=True,
            child=[
                Widget.Box(child=[icon, scale, arrow]),
                device_menu,
            ],
            css_classes=[f"volume-mainbox-{_type}"],
        )
