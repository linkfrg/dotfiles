import asyncio
from ignis import widgets
from ...qs_button import QSButton
from ...menu import Menu
from ignis.exceptions import RecorderPortalCaptureCanceled
from ignis.services.recorder import RecorderService, RecorderConfig

AUDIO_DEVICES = {
    "Internal audio": "default_output",
    "Microphone": "default_input",
    "Both sources": "default_output|default_input",
}

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
                            on_click=lambda x: asyncio.create_task(
                                self.__start_recording()
                            ),
                        ),
                    ],
                ),
            ],
        )

    async def __start_recording(self) -> None:
        self.set_reveal_child(False)

        config = RecorderConfig.new_from_options()

        if self._audio_switch.active:
            config.audio_devices = [AUDIO_DEVICES.get(self._dropdown.selected, "")]

        try:
            await recorder.start_recording(config=config)
        except RecorderPortalCaptureCanceled:
            pass


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
