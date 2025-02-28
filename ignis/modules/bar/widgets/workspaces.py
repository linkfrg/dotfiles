from ignis.widgets import Widget
from ignis.services.hyprland import HyprlandService, HyprlandWorkspace

hyprland = HyprlandService.get_default()


class WorkspaceButton(Widget.Button):
    def __init__(self, workspace: HyprlandWorkspace) -> None:
        super().__init__(
            css_classes=["workspace", "unset"],
            on_click=lambda x: workspace.switch_to(),
            halign="start",
            valign="center",
        )
        if workspace.id == hyprland.active_workspace.id:
            self.add_css_class("active")


def scroll_workspaces(direction: str) -> None:
    current = hyprland.active_workspace.id
    if direction == "up":
        target = current - 1
        hyprland.switch_to_workspace(target)
    else:
        target = current + 1
        if target == 11:
            return
        hyprland.switch_to_workspace(target)


class Workspaces(Widget.Box):
    def __init__(self):
        if hyprland.is_available:
            child = [
                Widget.EventBox(
                    on_scroll_up=lambda x: scroll_workspaces("up"),
                    on_scroll_down=lambda x: scroll_workspaces("down"),
                    css_classes=["workspaces"],
                    child=hyprland.bind_many(
                        ["workspaces", "active_workspace"],
                        transform=lambda workspaces, *_: [
                            WorkspaceButton(i) for i in workspaces
                        ],
                    ),
                )
            ]
        else:
            child = []
        super().__init__(child=child)
