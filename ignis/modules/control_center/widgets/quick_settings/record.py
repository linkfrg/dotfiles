from ignis import widgets
from ...qs_button import QSButton
from ...menu import Menu
from ignis.services.recorder import RecorderService

recorder = RecorderService.get_default()


class RecordMenu(Menu):
    def __init__(self):
        self._audio_switch = widgets.Switch(halign="end", hexpand=True, valign="center")
        self._dropdown = widgets.DropDown(
            items=["Internal audio", "Microphone", "Both sources"],
            css_classes=["record-dropdown"],
        )

        super().__init__(
            name="recording",
            child=[
                widgets.Icon(
                    image="media-record-symbolic",
                    pixel_size=36,
                    halign="center",
                    css_classes=["record-icon"],
                ),
                widgets.Label(
                    label="Start recording?",
                    halign="center",
                    style="font-size: 1.2rem;",
                ),
                widgets.Box(
                    style="margin-top: 0.5rem;",
                    child=[
                        widgets.Icon(
                            image="microphone-sensitivity-medium-symbolic",
                            pixel_size=20,
                            style="margin-right: 0.5rem;",
                        ),
                        widgets.Box(
                            vertical=True,
                            child=[
                                widgets.Label(
                                    label="Record audio",
                                    style="font-size: 1.1rem;",
                                    halign="start",
                                ),
                                self._dropdown,
                            ],
                        ),
                        self._audio_switch,
                    ],
                ),
                widgets.Box(
                    style="margin-top: 1rem;",
                    child=[
                        widgets.Button(
                            child=widgets.Label(label="Cancel"),
                            css_classes=["record-cancel-button", "unset"],
                            on_click=lambda x: self.set_reveal_child(False),  # type: ignore
                        ),
                        widgets.Button(
                            child=widgets.Label(label="Start recording"),
                            halign="end",
                            hexpand=True,
                            css_classes=["record-start-button", "unset"],
                            on_click=lambda x: self.__start_recording(),  # type: ignore
                        ),
                    ],
                ),
            ],
        )

    def __start_recording(self) -> None:
        self.set_reveal_child(False)
        microphone = False
        internal = False
        if self._audio_switch.active:
            if self._dropdown.selected == "Internal audio":
                internal = True
            elif self._dropdown.selected == "Microphone":
                microphone = True
            else:
                internal = True
                microphone = True

        recorder.start_recording(
            record_microphone=microphone, record_internal_audio=internal
        )


class RecordButton(QSButton):
    def __init__(self):
        record_menu = RecordMenu()

        super().__init__(
            label="Recording",
            icon_name="media-record-symbolic",
            on_activate=lambda x: record_menu.toggle(),
            on_deactivate=lambda x: recorder.stop_recording(),
            active=recorder.bind("active"),
            menu=record_menu,
        )
