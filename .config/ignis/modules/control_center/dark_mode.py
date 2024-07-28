from scripts.material import material
from .qs_button import QSButton


def dark_mode_button() -> QSButton:
    return QSButton(
        icon_name="night-light-symbolic",
        on_activate=lambda x: material.set_dark_mode(True),
        on_deactivate=lambda x: material.set_dark_mode(False),
        active=material.bind("dark-mode"),
    )
