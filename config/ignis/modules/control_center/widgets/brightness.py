import asyncio
from ignis.services.backlight import BacklightService
from ignis import widgets

backlight = BacklightService.get_default()


class Brightness(widgets.Box):
    def __init__(self):
        super().__init__(
            visible=backlight.bind("available"),
            hexpand=True,
            style="margin-top: 0.25rem;",
            child=[
                widgets.Icon(
                    image="display-brightness-symbolic",
                    css_classes=["material-slider-icon"],
                    pixel_size=18,
                ),
                widgets.Scale(
                    min=0,
                    max=backlight.max_brightness,
                    hexpand=True,
                    value=backlight.bind("brightness"),
                    css_classes=["material-slider"],
                    on_change=lambda x: asyncio.create_task(backlight.set_brightness_async(x.value)),
                ),
            ],
        )
