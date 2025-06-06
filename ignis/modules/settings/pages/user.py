import os
from ..elements import SettingsGroup, SettingsPage, SettingsEntry, FileRow
from ignis import widgets
from user_options import user_options


class UserEntry(SettingsEntry):
    def __init__(self):
        page = SettingsPage(
            name="User",
            groups=[
                widgets.Box(
                    halign="start",
                    style="margin-left: 2rem;",
                    child=[
                        widgets.Picture(
                            image=user_options.user.bind(
                                "avatar",
                                lambda value: "user-info"
                                if not os.path.exists(value)
                                else value,
                            ),
                            width=96,
                            height=96,
                            style="border-radius: 10rem;",
                        ),
                        widgets.Label(
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
                            dialog=widgets.FileDialog(
                                initial_path=user_options.user.bind("avatar"),
                                on_file_set=lambda x,
                                gfile: user_options.user.set_avatar(gfile.get_path()),
                            ),
                        )
                    ],
                ),
            ],
        )
        super().__init__(
            label="User",
            icon="user-available-symbolic",
            page=page,
        )
