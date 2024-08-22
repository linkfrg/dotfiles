from ignis.widgets import Widget
from gi.repository import GObject


class QSButton(Widget.Button):
    def __init__(
        self,
        label: str,
        icon_name: str,
        on_activate: callable = None,
        on_deactivate: callable = None,
        content: Widget.Revealer = None,
        **kwargs,
    ):
        self.on_activate = on_activate
        self.on_deactivate = on_deactivate
        self._active = False
        self._content = content
        super().__init__(
            child=Widget.Box(
                child=[
                    Widget.Icon(image=icon_name),
                    Widget.Label(label=label, css_classes=["qs-button-label"]),
                    Widget.Arrow(
                        halign="end",
                        hexpand=True,
                        pixel_size=20,
                        rotated=content.bind("reveal_child"),
                    )
                    if content
                    else None,
                ]
            ),
            on_click=self.__callback,
            css_classes=["qs-button", "unset"],
            hexpand=True,
            **kwargs,
        )

    def __callback(self, *args) -> None:
        if self.active:
            if self.on_deactivate:
                self.on_deactivate(self)
        else:
            if self.on_activate:
                self.on_activate(self)

    @GObject.Property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, value: bool) -> None:
        self._active = value
        if value:
            self.add_css_class("active")
        else:
            self.remove_css_class("active")

    @GObject.Property
    def content(self) -> Widget.Revealer:
        return self._content
