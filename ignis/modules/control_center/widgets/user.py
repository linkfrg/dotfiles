import os
from ignis import widgets
from ignis import utils
from ignis.window_manager import WindowManager
from ignis.services.fetch import FetchService
from user_options import user_options

fetch = FetchService.get_default()
window_manager = WindowManager.get_default()

def format_uptime(value: tuple[int, int, int, int]) -> str:
    days, hours, minutes, seconds = value
    if days:
        return f"up {days:02}:{hours:02}:{minutes:02}"
    else:
        return f"up {hours:02}:{minutes:02}"


class User(widgets.Box):
    def __init__(self):
        user_image = widgets.Picture(
            image=user_options.user.bind(
                "avatar",
                lambda value: "user-info" if not os.path.exists(value) else value,
            ),
            width=44,
            height=44,
            content_fit="cover",
            style="border-radius: 10rem;",
        )

        username = widgets.Box(
            child=[
                widgets.Label(
                    label=os.getenv("USER"), css_classes=["user-name"], halign="start"
                ),
                widgets.Label(
                    label=utils.Poll(
                        timeout=60 * 1000, callback=lambda x: fetch.uptime
                    ).bind("output", lambda value: format_uptime(value)),
                    halign="start",
                    css_classes=["user-name-secondary"],
                ),
            ],
            vertical=True,
            css_classes=["user-name-box"],
        )

        settings_button = widgets.Button(
            child=widgets.Icon(image="emblem-system-symbolic", pixel_size=20),
            halign="end",
            hexpand=True,
            css_classes=["user-settings", "unset"],
            on_click=lambda x: self.__on_settings_button_click(),
        )

        power_button = widgets.Button(
            child=widgets.Icon(image="system-shutdown-symbolic", pixel_size=20),
            halign="end",
            css_classes=["user-power", "unset"],
            on_click=lambda x: window_manager.toggle_window("ignis_POWERMENU"),
        )
        super().__init__(
            child=[user_image, username, settings_button, power_button],
            css_classes=["user"],
        )

    def __on_settings_button_click(self) -> None:
        window = window_manager.get_window("ignis_SETTINGS")
        window.visible = not window.visible  # type: ignore
