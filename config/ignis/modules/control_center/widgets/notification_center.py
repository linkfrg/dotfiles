from gi.repository import (  # type: ignore  # pyright: ignore
    IgnisNotificationsGLib,
)
from ignis import utils, widgets

from setup import get_notification_service

from ...shared_widgets import NotificationWidget

service = get_notification_service()


class Popup(widgets.Revealer):
    def __init__(self, notification: IgnisNotificationsGLib.Notification, **kwargs):
        widget = NotificationWidget(notification)
        super().__init__(child=widget, transition_type="slide_down", **kwargs)

        notification.connect("closed", lambda x, _reason: self.destroy())

    def destroy(self):
        self.reveal_child = False
        utils.Timeout(self.transition_duration, self.unparent)


class NotificationList(widgets.Box):
    __gtype_name__ = "NotificationList"

    def __init__(self):
        super().__init__(
            vertical=True,
            vexpand=True,
            css_classes=["rec-unset"],
        )

        self._no_notifications: bool = False

        widgets = self.__load_notifications()

        if len(widgets) > 0:
            self.set_child(widgets)
        else:
            self.__set_no_notifications()

        service.connect(
            "notified",
            lambda x, id, notification, replace: self.__on_notified(notification),
        )

        service.connect("notifications-cleared", lambda x: self.__clear())

        service.connect(
            "closed",
            lambda _, __, ___: (
                self.__set_no_notifications()
                if len(service.get_notifications()) == 0
                else None
            ),
        )

    def __on_notified(self, notification: IgnisNotificationsGLib.Notification) -> None:
        if self._no_notifications:
            self.set_child([])
            self._no_notifications = False

        notify = Popup(notification)
        self.prepend(notify)
        notify.reveal_child = True

    def __clear(self) -> None:
        if len(self.get_child()) != 0:
            # bruh
            timeout = self.get_child()[0].get_transition_duration()

            for i in self.get_child():
                i.destroy()

            utils.Timeout(timeout, self.__set_no_notifications)

        else:
            self.__set_no_notifications()

    def __set_no_notifications(self) -> None:

        label = widgets.Label(
            label="No notifications",
            valign="center",
            vexpand=True,
            css_classes=["notification-center-info-label"],
        )

        self.set_child([label])
        self._no_notifications = True

    def __load_notifications(self) -> list[widgets.Label | Popup]:
        notifications = service.get_notifications()
        notifications.reverse()

        contents: list[widgets.Label | Popup] = [
            Popup(i, reveal_child=True) for i in notifications
        ]

        return contents


class NotificationCenter(widgets.Box):
    __gtype_name__ = "NotificationCenter"

    def __init__(self):
        super().__init__(
            vertical=True,
            vexpand=True,
            css_classes=["notification-center"],
            child=[
                widgets.Box(
                    css_classes=["notification-center-header", "rec-unset"],
                    child=[
                        widgets.Label(
                            # label=notifications.bind(
                            #     "notifications", lambda value: str(len(value))
                            # ),
                            label=str(len(service.get_notifications())),
                            css_classes=["notification-count"],
                            setup=lambda x: service.connect(
                                "notify::notifications",
                                lambda _, __: x.set_label(
                                    str(len(service.get_notifications()))
                                ),
                            ),
                        ),
                        widgets.Label(
                            label="notifications",
                            css_classes=["notification-header-label"],
                        ),
                        widgets.Button(
                            child=widgets.Label(label="Clear all"),
                            halign="end",
                            hexpand=True,
                            on_click=lambda x: service.clear_notifications_async(
                                None,
                                lambda x, res: service.clear_notifications_finish(res),
                            ),
                            css_classes=["notification-clear-all"],
                        ),
                    ],
                ),
                widgets.Scroll(
                    child=NotificationList(),
                    vexpand=True,
                ),
            ],
        )
