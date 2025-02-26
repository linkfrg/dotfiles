from ignis.widgets import Widget
from ignis.services.audio import AudioService, Stream

audio = AudioService.get_default()


class MaterialVolumeSlider(Widget.Scale):
    def __init__(self, stream: Stream, **kwargs):
        super().__init__(
            value=stream.bind_many(
                ["volume", "is_muted"],
                lambda volume, is_muted: 0 if is_muted or volume is None else volume,
            ),
            css_classes=["material-slider"],
            hexpand=True,
            step=5,
            **kwargs,
        )
