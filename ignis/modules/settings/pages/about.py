from ..elements import SettingsPage, SettingsRow, SettingsEntry, SettingsGroup
from ignis import utils
from ignis import widgets
from ignis.services.fetch import FetchService
from ignis._version import __version__
from user_options import user_options

fetch = FetchService.get_default()

def get_os_logo(dark_mode: bool) -> str | None:
    if dark_mode:
        return fetch.os_logo_text_dark or fetch.os_logo_dark or fetch.os_logo
    else:
        return fetch.os_logo_text or fetch.os_logo

class AboutEntry(SettingsEntry):
    def __init__(self):
        page = SettingsPage(
            name="About",
            groups=[
                widgets.Icon(
                    icon_name=user_options.material.bind(
                        "dark_mode",
                        transform=lambda value: get_os_logo(value),
                    ),
                    pixel_size=200,
                ),
                SettingsGroup(
                    name="Info",
                    rows=[
                        SettingsRow(label="OS", sublabel=fetch.os_name),
                        SettingsRow(
                            label="Ignis version", sublabel=__version__
                        ),
                        SettingsRow(label="Session type", sublabel=fetch.session_type),
                        SettingsRow(
                            label="Wayland compositor", sublabel=fetch.current_desktop
                        ),
                        SettingsRow(label="Kernel", sublabel=fetch.kernel),
                    ],
                ),
            ],
        )
        super().__init__(
            label="About",
            icon="help-about-symbolic",
            page=page,
        )
