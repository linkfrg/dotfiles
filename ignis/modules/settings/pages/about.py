from ..elements import SettingsPage, SettingsRow, SettingsEntry, SettingsGroup
from ignis.utils import Utils
from ignis.widgets import Widget
from services.material import MaterialService
from ignis.services.fetch import FetchService

fetch = FetchService.get_default()
material = MaterialService.get_default()


class AboutEntry(SettingsEntry):
    def __init__(self):
        page = SettingsPage(
            name="About",
            groups=[
                Widget.Box(
                    child=[
                        Widget.Picture(
                            image=material.bind(
                                "dark_mode",
                                transform=lambda value: fetch.os_logo_text_dark
                                if value
                                else fetch.os_logo_text,
                            ),
                            width=300,
                            height=100,
                        )
                    ],
                    halign="center",
                    width_request=300,
                    height_request=100,
                ),
                SettingsGroup(
                    name="Info",
                    rows=[
                        SettingsRow(label="OS", sublabel=fetch.os_name),
                        SettingsRow(
                            label="Ignis version", sublabel=Utils.get_ignis_version()
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
