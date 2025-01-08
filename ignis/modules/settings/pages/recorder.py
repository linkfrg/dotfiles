from ..elements import (
    SpinRow,
    SettingsPage,
    SettingsGroup,
    EntryRow,
    FileRow,
    SettingsEntry,
)
from ignis.widgets import Widget
from ignis.options import options


class RecorderEntry(SettingsEntry):
    def __init__(self):
        page = SettingsPage(
            name="Recorder",
            groups=[
                SettingsGroup(
                    name="General",
                    rows=[
                        SpinRow(
                            label="Recording bitrate",
                            sublabel="Affects the recording quality",
                            value=options.recorder.bind("bitrate"),
                            max=640000,
                            width=150,
                            on_change=lambda x, value: options.recorder.set_bitrate(
                                int(value)
                            ),
                            step=1000,
                        ),
                        FileRow(
                            label="Recording path",
                            button_label=options.recorder.bind("default_file_location"),
                            dialog=Widget.FileDialog(
                                on_file_set=lambda x,
                                file: options.recorder.set_default_file_location(
                                    file.get_path()
                                ),
                                select_folder=True,
                                initial_path=options.recorder.default_file_location,
                            ),
                        ),
                        EntryRow(
                            label="Recording filename",
                            sublabel="Support time formatting",
                            text=options.recorder.bind("default_filename"),
                            on_change=lambda x: options.recorder.set_default_filename(
                                x.text
                            ),
                            width=200,
                        ),
                    ],
                )
            ],
        )
        super().__init__(
            label="Recorder",
            icon="media-record-symbolic",
            page=page,
        )
