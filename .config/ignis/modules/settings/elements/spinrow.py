from ignis.widgets import Widget
from .row import SettingsRow


class SpinRow(SettingsRow):
    def __init__(
        self,
        value: int = None,
        on_change: callable = None,
        min: int = None,
        max: int = None,
        step: int = None,
        width: int = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self._spin_button = Widget.SpinButton(
            value=value,
            on_change=on_change,
            min=min,
            max=max,
            halign="end",
            valign="center",
            width_request=width,
            hexpand=True,
            step=step,
        )
        self.child.append(self._spin_button)
