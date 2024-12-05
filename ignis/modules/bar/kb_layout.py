from ignis.widgets import Widget
from ignis.services.hyprland import HyprlandService

hyprland = HyprlandService.get_default()


def kb_layout():
    return Widget.Button(
        css_classes=["kb-layout", "unset"],
        on_click=lambda x: hyprland.switch_kb_layout(),
        visible=hyprland.is_available,
        child=Widget.Label(
            label=hyprland.bind("kb_layout", transform=lambda value: value[:2].lower())
        ),
    )
