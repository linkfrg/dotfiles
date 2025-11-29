from ignis import widgets
from ignis import utils
from ignis.services.audio import AudioService
from ..shared_widgets import MaterialVolumeSlider

audio = AudioService.get_default()


class VolumeOsd(widgets.Window):
    def __init__(self):
        super().__init__(
            layer="overlay",
            anchor=["bottom"],
            namespace="ignis_OSD",
            visible=False,
            css_classes=["rec-unset"],
            child=widgets.Box(
                css_classes=["osd"],
                child=[
                    widgets.Icon(
                        pixel_size=26,
                        style="margin-right: 0.5rem;",
                        image=audio.speaker.bind("icon_name"),
                    ),
                    MaterialVolumeSlider(stream=audio.speaker, sensitive=False),
                ],
            ),
        )

    def toggle(self) -> None:
        self.visible = True
        self.__hide()

    @utils.debounce(3000)
    def __hide(self) -> None:
        self.visible = False

    def increase_volume(self) -> None:
        self.toggle()
        audio.speaker.set_volume(min(audio.speaker.volume + 5, 100))

    def decrease_volume(self) -> None:
        self.toggle()
        audio.speaker.set_volume(max(audio.speaker.volume - 5, 0))

    def toggle_mute(self) -> None:
        self.toggle()
        audio.speaker.is_muted = not audio.speaker.is_muted
