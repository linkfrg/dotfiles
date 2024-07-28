from ignis.widgets import Widget
from gi.repository import GObject


class QSButton(Widget.Button):
    def __init__(
        self,
        icon_name: str,
        on_activate: callable = None,
        on_deactivate: callable = None,
        **kwargs,
    ):
        self.on_activate = on_activate
        self.on_deactivate = on_deactivate
        self._active = False
        super().__init__(
            child=Widget.Icon(image=icon_name),
            on_click=self.__callback,
            css_classes=["qs-button", "unset"],
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
            self.add_css_class('active')
        else:
            self.remove_css_class('active')
