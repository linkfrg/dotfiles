from .qs_button import QSButton
from ignis.services.notifications import NotificationService

notifications = NotificationService.get_default()


def dnd_button() -> QSButton:
    return QSButton(
        label=notifications.bind("dnd", lambda value: "Silent" if value else "Noisy"),
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
