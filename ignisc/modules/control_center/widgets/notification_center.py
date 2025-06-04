from ignis.widgets import Widget
from ignis.services.notifications import Notification, NotificationService
from ignis.utils import Utils
from gi.repository import GLib  # type: ignore
from ...shared_widgets import NotificationWidget

notifications = NotificationService.get_default()


class Popup(Widget.Revealer):
    def __init__(self, notification: Notification, **kwargs):
        widget = NotificationWidget(notification)
        super().__init__(child=widget, transition_type="slide_down", **kwargs)

        notification.connect("closed", lambda x: self.destroy())

    def destroy(self):
        self.reveal_child = False
        Utils.Timeout(self.transition_duration, self.unparent)


class NotificationList(Widget.Box):
    __gtype_name__ = "NotificationList"

    def __init__(self):
        loading_notifications_label = Widget.Label(
            label="Loading notifications...",
            valign="center",
            vexpand=True,
            css_classes=["notification-center-info-label"],
        )

        super().__init__(
            vertical=True,
            child=[loading_notifications_label],
            vexpand=True,
            css_classes=["rec-unset"],
            setup=lambda self: notifications.connect(
                "notified",
                lambda x, notification: self.__on_notified(notification),
            ),
        )

        Utils.ThreadTask(
            self.__load_notifications,
            lambda result: self.set_child(result),
        ).run()

    def __on_notified(self, notification: Notification) -> None:
        notify = Popup(notification)
        self.prepend(notify)
        notify.reveal_child = True

    def __load_notifications(self) -> list[Widget.Label | Popup]:
        widgets: list[Widget.Label | Popup] = []
        for i in notifications.notifications:
            GLib.idle_add(lambda i=i: widgets.append(Popup(i, reveal_child=True)))

        widgets.append(
            Widget.Label(
                label="No notifications",
                valign="center",
                vexpand=True,
                visible=notifications.bind(
                    "notifications", lambda value: len(value) == 0
                ),
                css_classes=["notification-center-info-label"],
            )
        )
        return widgets


class NotificationCenter(Widget.Box):
    __gtype_name__ = "NotificationCenter"

    def __init__(self):
        super().__init__(
            vertical=True,
            vexpand=True,
            css_classes=["notification-center"],
            child=[
                Widget.Box(
                    css_classes=["notification-center-header", "rec-unset"],
                    child=[
                        Widget.Label(
                            label=notifications.bind(
                                "notifications", lambda value: str(len(value))
                            ),
                            css_classes=["notification-count"],
                        ),
                        Widget.Label(
                            label="notifications",
                            css_classes=["notification-header-label"],
                        ),
                        Widget.Button(
                            child=Widget.Label(label="Clear all"),
                            halign="end",
                            hexpand=True,
                            on_click=lambda x: notifications.clear_all(),
                            css_classes=["notification-clear-all"],
                        ),
                    ],
                ),
                Widget.Scroll(
                    child=NotificationList(),
                    vexpand=True,
                ),
            ],
        )
