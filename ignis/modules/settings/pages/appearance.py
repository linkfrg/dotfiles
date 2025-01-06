import os
from services.material import MaterialService
from ..elements import SwitchRow, SettingsPage, SettingsGroup, FileRow, SettingsEntry
from ignis.widgets import Widget
from user_options import user_options
from ignis.options import options

material = MaterialService.get_default()


class AppearanceEntry(SettingsEntry):
    def __init__(self):
        page = SettingsPage(
            name="Appearance",
            groups=[
                SettingsGroup(
                    name=None,
                    rows=[
                        Widget.ListBoxRow(
                            child=Widget.Picture(
                                image=options.wallpaper.bind("wallpaper_path"),
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
                            active=user_options.material.bind("dark_mode"),
                            on_change=lambda x,
                            state: user_options.material.set_dark_mode(state),
                            style="margin-top: 1rem;",
                        ),
                        FileRow(
                            label="Wallpaper path",
                            button_label=os.path.basename(
                                options.wallpaper.wallpaper_path
                            )
                            if options.wallpaper.wallpaper_path
                            else None,
                            dialog=Widget.FileDialog(
                                on_file_set=lambda x, file: material.generate_colors(
                                    file.get_path()
                                ),
                                initial_path=options.wallpaper.bind("wallpaper_path"),
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
        super().__init__(
            label="Appearance",
            icon="preferences-desktop-wallpaper-symbolic",
            page=page,
        )
