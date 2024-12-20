from ignis.widgets import Widget
from ignis.utils import Utils
from ignis.services.audio import AudioService

audio = AudioService.get_default()


class OSD(Widget.Window):
    def __init__(self):
        super().__init__(
            layer="overlay",
            anchor=["bottom"],
            namespace="ignis_OSD",
            visible=False,
            css_classes=["rec-unset"],
            child=Widget.Box(
                css_classes=["osd"],
                child=[
                    Widget.Icon(
                        pixel_size=26,
                        style="margin-right: 0.5rem;",
                        image=audio.speaker.bind("icon_name"),
                    ),
                    Widget.Scale(
                        value=audio.speaker.bind("volume"),
                        css_classes=["material-slider"],
                        sensitive=False,
                        hexpand=True,
                    ),
                ],
            ),
        )

    def set_property(self, property_name, value):
        if property_name == "visible":
            self.__update_visible()

        super().set_property(property_name, value)

    @Utils.debounce(3000)
    def __update_visible(self) -> None:
        super().set_property("visible", False)
