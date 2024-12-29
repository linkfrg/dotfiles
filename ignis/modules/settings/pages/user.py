import os
from ..elements import SettingsGroup, SettingsPage, SettingsEntry, FileRow
from ignis.widgets import Widget
from options import avatar_opt


class UserEntry(SettingsEntry):
    def __init__(self):
        page = SettingsPage(
            name="User",
            groups=[
                Widget.Box(
                    halign="start",
                    style="margin-left: 2rem;",
                    child=[
                        Widget.Picture(
                            image=avatar_opt.bind(
                                "value",
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
                                initial_path=avatar_opt.bind("value"),
                                on_file_set=lambda x, gfile: avatar_opt.set_value(
                                    gfile.get_path()
                                ),
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
