from ignis.widgets import Widget
from ignis.services import Service
hyprland = Service.get("hyprland")

def kb_layout():
    return Widget.Button(
        css_classes=["kb-layout", "unset"],
        on_click=lambda x: hyprland.switch_kb_layout(),
        child=Widget.Label(
            label=hyprland.bind("kb_layout", transform=lambda value: value[:2].lower())
        ),
    )
