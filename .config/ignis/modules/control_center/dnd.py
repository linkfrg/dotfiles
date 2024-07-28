from .qs_button import QSButton
from ignis.services import Service
from ignis.services.notifications import NotificationService

notifications: NotificationService = Service.get("notifications")


def dnd_button() -> QSButton:
    return QSButton(
        icon_name=notifications.bind(
            "dnd",
            transform=lambda value: "notification-disabled-symbolic"
            if value
            else "notification-symbolic",
        ),
        on_activate=lambda x: notifications.set_dnd(not notifications.dnd),
        on_deactivate=lambda x: notifications.set_dnd(not notifications.dnd),
        active=notifications.bind("dnd"),
    )
