from ignis.services.recorder import RecorderService
from .elements import (
    SpinRow,
    SettingsPage,
    SettingsGroup,
    EntryRow,
    FileRow,
    SettingsEntry,
)
from ignis.widgets import Widget

recorder = RecorderService.get_default()


def recorder_entry(active_page):
    recorder_page = SettingsPage(
        name="Recorder",
        groups=[
            SettingsGroup(
                name="General",
                rows=[
                    SpinRow(
                        label="Recording bitrate",
                        sublabel="Affects the recording quality",
                        value=recorder.bind("bitrate"),
                        max=640000,
                        width=150,
                        on_change=lambda x, value: recorder.set_bitrate(int(value)),
                        step=1000,
                    ),
                    FileRow(
                        label="Recording path",
                        button_label=recorder.bind("default_file_location"),
                        dialog=Widget.FileDialog(
                            on_file_set=lambda x,
                            file: recorder.set_default_file_location(file.get_path()),
                            select_folder=True,
                            initial_path=recorder.default_file_location,
                        ),
                    ),
                    EntryRow(
                        label="Recording filename",
                        sublabel="Support time formatting",
                        text=recorder.bind("default_filename"),
                        on_change=lambda x: recorder.set_default_filename(x.text),
                        width=200,
                    ),
                ],
            )
        ],
    )

    return SettingsEntry(
        label="Recorder",
        icon="media-record-symbolic",
        active_page=active_page,
        page=recorder_page,
    )
