import os
from services.material import MaterialService
from .elements import SwitchRow, SettingsPage, SettingsGroup, FileRow, SettingsEntry
from ignis.widgets import Widget
from ignis.services.wallpaper import WallpaperService

wallpaper = WallpaperService.get_default()
material = MaterialService.get_default()


def appearance_entry(active_page):
    appearance_page = SettingsPage(
        name="Appearance",
        groups=[
            SettingsGroup(
                name=None,
                rows=[
                    Widget.ListBoxRow(
                        child=Widget.Picture(
                            image=wallpaper.bind("wallpaper"),
                            width=1920 // 4,
                            height=1080 // 4,
                            halign="center",
                            style="border-radius: 1rem;",
                            content_fit="cover",
                        ),
                        selectable=False,
                        activatable=False,
                    ),
                    SwitchRow(
                        label="Dark mode",
                        active=material.bind("dark_mode"),
                        on_change=lambda x, state: material.set_dark_mode(state),
                        style="margin-top: 1rem;",
                    ),
                    FileRow(
                        label="Wallpaper path",
                        button_label=os.path.basename(wallpaper.wallpaper)
                        if wallpaper.wallpaper
                        else None,
                        dialog=Widget.FileDialog(
                            on_file_set=lambda x, file: material.generate_colors(
                                file.get_path()
                            ),
                            initial_path=wallpaper.bind("wallpaper"),
                            filters=[
                                Widget.FileFilter(
                                    mime_types=["image/jpeg", "image/png"],
                                    default=True,
                                    name="Images JPEG/PNG",
                                )
                            ],
                        ),
                    ),
                ],
            )
        ],
    )
    return SettingsEntry(
        label="Appearance",
        icon="preferences-desktop-wallpaper-symbolic",
        active_page=active_page,
        page=appearance_page,
    )
