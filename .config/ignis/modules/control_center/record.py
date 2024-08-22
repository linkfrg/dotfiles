from ignis.widgets import Widget
from .qs_button import QSButton
from ignis.services import Service
from ignis.services.recorder import RecorderService

recorder: RecorderService = Service.get("recorder")


def record_menu() -> Widget.Revealer:
    record_audio_switch = Widget.Switch(halign="end", hexpand=True, valign="center")
    dropdown = Widget.DropDown(
        items=["Internal audio", "Microphone", "Both sources"],
        css_classes=["record-dropdown"],
    )

    def start_recording(x):
        record_menu_widget.set_reveal_child(False)
        microphone = False
        internal = False
        if record_audio_switch.active:
            if dropdown.selected == "Internal audio":
                internal = True
            elif dropdown.selected == "Microphone":
                microphone = True
            else:
                internal = True
                microphone = True

        recorder.start_recording(
            record_microphone=microphone, record_internal_audio=internal
        )

    record_menu_widget = Widget.Revealer(
        transition_duration=300,
        transition_type="slide_down",
        child=Widget.Box(
            css_classes=["record-menu"],
            vertical=True,
            child=[
                Widget.Icon(
                    image="media-record-symbolic",
                    pixel_size=36,
                    halign="center",
                    css_classes=["record-icon"],
                ),
                Widget.Label(
                    label="Start recording?",
                    halign="center",
                    style="font-size: 1.2rem;",
                ),
                Widget.Box(
                    style="margin-top: 0.5rem;",
                    child=[
                        Widget.Icon(
                            image="microphone-sensitivity-medium-symbolic",
                            pixel_size=20,
                            style="margin-right: 0.5rem;",
                        ),
                        Widget.Box(
                            vertical=True,
                            child=[
                                Widget.Label(
                                    label="Record audio",
                                    style="font-size: 1.1rem;",
                                    halign="start",
                                ),
                                dropdown,
                            ],
                        ),
                        record_audio_switch,
                    ],
                ),
                Widget.Box(
                    style="margin-top: 1rem;",
                    child=[
                        Widget.Button(
                            child=Widget.Label(label="Cancel"),
                            css_classes=["record-cancel-button", "unset"],
                            on_click=lambda x: record_menu_widget.set_reveal_child(
                                False
                            ),
                        ),
                        Widget.Button(
                            child=Widget.Label(label="Start recording"),
                            halign="end",
                            hexpand=True,
                            css_classes=["record-start-button", "unset"],
                            on_click=start_recording,
                        ),
                    ],
                ),
            ],
        ),
    )
    return record_menu_widget


def record_control() -> QSButton:
    record_menu_widget = record_menu()
    return QSButton(
        label="Recording",
        icon_name="media-record-symbolic",
        on_activate=lambda x: record_menu_widget.toggle(),
        on_deactivate=lambda x: recorder.stop_recording(),
        active=recorder.bind("active"),
        content=record_menu_widget,
    )
