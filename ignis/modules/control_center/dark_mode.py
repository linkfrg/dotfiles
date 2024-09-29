from services.material import MaterialService
from .qs_button import QSButton

material = MaterialService.get_default()


def dark_mode_button() -> QSButton:
    return QSButton(
        label="Dark",
        icon_name="night-light-symbolic",
        on_activate=lambda x: material.set_dark_mode(True),
        on_deactivate=lambda x: material.set_dark_mode(False),
        active=material.bind("dark-mode"),
    )
