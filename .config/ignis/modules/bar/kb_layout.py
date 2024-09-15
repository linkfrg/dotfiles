from ignis.widgets import Widget
from ignis.exceptions import HyprlandIPCNotFoundError
from ignis.services.hyprland import HyprlandService

try:
    hyprland = HyprlandService.get_default()

    def kb_layout():
        return Widget.Button(
            css_classes=["kb-layout", "unset"],
            on_click=lambda x: hyprland.switch_kb_layout(),
            child=Widget.Label(
                label=hyprland.bind(
                    "kb_layout", transform=lambda value: value[:2].lower()
                )
            ),
        )
except HyprlandIPCNotFoundError:

    def kb_layout():
        return
