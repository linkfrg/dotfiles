import os
from .elements import SettingsGroup, SettingsPage, SettingsEntry, FileRow
from ignis.widgets import Widget
from ignis.services import Service

options = Service.get("options")


def user_entry(active_page):
    page = SettingsPage(
        name="User",
        groups=[
            Widget.Box(
                halign="start",
                style="margin-left: 2rem;",
                child=[
                    Widget.Picture(
                        image=options.bind_option("user_avatar"),
                        width=96,
                        height=96,
                        style="border-radius: 10rem;",
                    ),
                    Widget.Label(
                        label=os.getenv("USER"), css_classes=["settings-user-name"]
                    ),
                ],
            ),
            SettingsGroup(
                style="margin-top: 2rem;",
                valign="start",
                name="General",
                vexpand=True,
                rows=[
                    FileRow(
                        label="Avatar",
                        dialog=Widget.FileDialog(
                            initial_path=options.bind_option("user_avatar"),
                            on_file_set=lambda x, gfile: options.set_option(
                                "user_avatar", gfile.get_path()
                            )
                        )
                    )
                ],
            ),
        ],
    )

    return SettingsEntry(
        label="User",
        icon="user-available-symbolic",
        active_page=active_page,
        page=page,
    )
