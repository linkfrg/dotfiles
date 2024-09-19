import os
from .elements import SettingsGroup, SettingsPage, SettingsEntry, FileRow
from ignis.widgets import Widget
from options import USER_OPT_GROUP


def user_entry(active_page):
    page = SettingsPage(
        name="User",
        groups=[
            Widget.Box(
                halign="start",
                style="margin-left: 2rem;",
                child=[
                    Widget.Picture(
                        image=USER_OPT_GROUP.bind_option(
                            "avatar",
                            lambda value: "user-info"
                            if not os.path.exists(value)
                            else value,
                        ),
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
                            initial_path=USER_OPT_GROUP.bind_option("avatar"),
                            on_file_set=lambda x, gfile: USER_OPT_GROUP.set_option(
                                "avatar", gfile.get_path()
                            ),
                        ),
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
