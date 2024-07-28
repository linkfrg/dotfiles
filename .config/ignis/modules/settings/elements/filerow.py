from ignis.widgets import Widget
from .row import SettingsRow


class FileRow(SettingsRow):
    def __init__(
        self,
        dialog: Widget.FileDialog,
        button_label: str = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self._button = Widget.FileChooserButton(
            dialog=dialog,
            label=Widget.Label(label=button_label, ellipsize="start", max_width_chars=20),
            hexpand=True,
            halign="end",
        )
        
        self.child.append(self._button)
