from ...qs_button import QSButton
from user_options import user_options


class DarkModeButton(QSButton):
    __gtype_name__ = "DarkModeButton"

    def __init__(self):
        super().__init__(
            label="Dark",
            icon_name="night-light-symbolic",
            on_activate=lambda x: user_options.material.set_dark_mode(True),
            on_deactivate=lambda x: user_options.material.set_dark_mode(False),
            active=user_options.material.bind("dark_mode"),
        )
