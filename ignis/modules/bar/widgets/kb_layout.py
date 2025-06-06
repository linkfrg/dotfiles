from ignis import widgets
from ignis.services.hyprland import HyprlandService

hyprland = HyprlandService.get_default()


class KeyboardLayout(widgets.Button):
    def __init__(self):
        super().__init__(
            css_classes=["kb-layout", "unset"],
            on_click=lambda x: hyprland.main_keyboard.switch_layout("next"),
            visible=hyprland.is_available,
            child=widgets.Label(
                label=hyprland.main_keyboard.bind(
                    "active_keymap", transform=lambda value: value[:2].lower()
                )
            ),
        )
