from .elements import SettingsPage, SettingsRow, SettingsEntry
from ignis.utils import Utils
from ignis.widgets import Widget
from scripts.material import material
from ignis.services import Service

fetch = Service.get("fetch")

def about_entry(active_page):
    about_page = SettingsPage(
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
            SettingsRow(label="OS", sublabel=fetch.os_name),
            SettingsRow(label="Ignis version", sublabel=Utils.get_ignis_version()),
            SettingsRow(label="Session type", sublabel=fetch.session_type),
            SettingsRow(label="Wayland compositor", sublabel=fetch.current_desktop),
            SettingsRow(label="Kernel", sublabel=fetch.kernel),
        ],
    )
    return SettingsEntry(
        label="About",
        icon="help-about-symbolic",
        active_page=active_page,
        page=about_page,
    )
