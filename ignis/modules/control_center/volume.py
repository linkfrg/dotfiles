from ignis.widgets import Widget
from ignis.utils import Utils
from ignis.services.audio import AudioService, Stream

audio = AudioService.get_default()


def volume_scale(stream: Stream) -> Widget.Scale:
    return Widget.Scale(
        css_classes=["material-slider"],
        value=stream.bind("volume"),
        step=5,
        hexpand=True,
        on_change=lambda x: stream.set_volume(x.value),
        sensitive=stream.bind("is_muted", lambda value: not value),
    )


def device_entry(stream: Stream, _type: str) -> Widget.Button:
    widget = Widget.Button(
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
        on_click=lambda x: setattr(audio, _type, stream),
    )
    stream.connect("removed", lambda x: widget.unparent())

    return widget


def device_list(
    header_label: str, header_icon: str, _type: str, **kwargs
) -> Widget.Revealer:
    box = Widget.Box(
        css_classes=["control-center-menu"],
        vertical=True,
        child=[
            Widget.Box(
                child=[
                    Widget.Icon(image=header_icon, pixel_size=24),
                    Widget.Label(
                        label=header_label,
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
                    lambda x, stream: self.append(device_entry(stream, _type)),
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
                on_click=lambda x: Utils.exec_sh_async("pavucontrol"),
            ),
        ],
        **kwargs,
    )

    return Widget.Revealer(
        child=box, transition_type="slide_down", transition_duration=300
    )


def volume_icon(stream: Stream) -> Widget.Button:
    return Widget.Button(
        child=Widget.Icon(
            image=stream.bind("icon_name"),
            pixel_size=18,
        ),
        css_classes=["material-slider-icon", "unset", "hover-surface"],
        on_click=lambda x: stream.set_is_muted(not stream.is_muted),
    )


def device_list_arrow(device_list: Widget.Revealer) -> Widget.Button:
    return Widget.ArrowButton(
        arrow=Widget.Arrow(pixel_size=20),
        css_classes=["material-slider-arrow", "hover-surface"],
        on_click=lambda x: device_list.toggle(),
    )


def volume_control():
    speakers_list = device_list(
        header_label="Sound Output",
        header_icon="audio-headphones-symbolic",
        _type="speaker",
        style="margin-bottom: 1rem;",
    )

    microphones_list = device_list(
        header_label="Sound Input",
        header_icon="microphone-sensitivity-high-symbolic",
        _type="microphone",
    )

    speaker_icon = volume_icon(audio.speaker)
    microphone_icon = volume_icon(audio.microphone)

    speaker_scale = volume_scale(audio.speaker)
    microphone_scale = volume_scale(audio.microphone)

    speaker_arrow = device_list_arrow(speakers_list)
    microphone_arrow = device_list_arrow(microphones_list)

    speaker_control = Widget.Box(
        vertical=True,
        child=[
            Widget.Box(child=[speaker_icon, speaker_scale, speaker_arrow]),
            speakers_list,
        ],
        style="margin-top: 1rem;",
    )

    microphone_control = Widget.Box(
        vertical=True,
        child=[
            Widget.Box(child=[microphone_icon, microphone_scale, microphone_arrow]),
            microphones_list,
        ],
        style="margin-top: 0.25rem;",
    )

    return Widget.Box(
        vertical=True,
        child=[speaker_control, microphone_control],
    )
