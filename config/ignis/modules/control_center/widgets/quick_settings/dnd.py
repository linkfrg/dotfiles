from ignis.options import options

from ...qs_button import QSButton

# notifications = NotificationService.get_default()


class DNDButton(QSButton):
    __gtype_name__ = "DNDButton"

    def __init__(self):
        super().__init__(
            label="test",
            icon_name="lol",
            # label=options.notifications.bind(
            #     "dnd", lambda value: "Silent" if value else "Noisy"
            # ),
            # icon_name=options.notifications.bind(
            #     "dnd",
            #     transform=lambda value: "notification-disabled-symbolic"
            #     if value
            #     else "notification-symbolic",
            # ),
            # on_activate=lambda x: self.__activate(True),
            # on_deactivate=lambda x: self.__activate(False),
            # active=options.notifications.bind("dnd"),
        )

    def __activate(self, state: bool) -> None:
        options.notifications.dnd = state
