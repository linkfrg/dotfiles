from ignis.services.backlight import BacklightService
from ignis.widgets import Widget

backlight = BacklightService.get_default()


def brightness_slider() -> Widget.Scale:
    return Widget.Box(
        visible=backlight.bind("available"),
        hexpand=True,
        style="margin-top: 0.25rem;",
        child=[
            Widget.Icon(
                image="display-brightness-symbolic",
                css_classes=["material-slider-icon"],
                pixel_size=18,
            ),
            Widget.Scale(
                min=0,
                max=backlight.max_brightness,
                hexpand=True,
                value=backlight.bind("brightness"),
                css_classes=["material-slider"],
                on_change=lambda x: backlight.set_brightness(x.value),
            ),
        ],
    )
