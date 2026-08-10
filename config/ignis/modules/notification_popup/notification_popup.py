from gi.repository import IgnisNotificationsGLib
from ignis import utils, widgets

from setup import get_notification_service

from ..shared_widgets import NotificationWidget

service = get_notification_service()

POPUPS = []


class Popup(widgets.Box):
    def __init__(
        self,
        box: "PopupBox",
        window: "NotificationPopup",
        notification: IgnisNotificationsGLib.Notification,
    ):
        self._box = box
        self._window = window

        widget = NotificationWidget(notification)
        widget.css_classes = ["notification-popup"]

        self._inner = widgets.Revealer(transition_type="slide_left", child=widget)
        self._outer = widgets.Revealer(transition_type="slide_down", child=self._inner)

        super().__init__(child=[self._outer], halign="end")

        notification.connect("closed", lambda x, reason: self.destroy())
        utils.Timeout(3000, self.destroy)

    def destroy(self):
        def box_destroy():
            self.unparent()

            if self in POPUPS:
                POPUPS.remove(self)

            if len(POPUPS) == 0:
                self._window.visible = False

        def outer_close():
            self._outer.reveal_child = False
            utils.Timeout(self._outer.transition_duration, box_destroy)

        self._inner.transition_type = "crossfade"
        self._inner.reveal_child = False
        utils.Timeout(self._outer.transition_duration, outer_close)


class PopupBox(widgets.Box):
    def __init__(self, window: "NotificationPopup", monitor: int):
        self._window = window
        self._monitor = monitor

        super().__init__(
            vertical=True,
            valign="start",
        )

        service.connect(
            "notified",
            lambda x, id, notification, replace: self.__on_notified(notification),
        )

    def __on_notified(
        self,
        notification: IgnisNotificationsGLib.Notification,
    ) -> None:
        popup = Popup(box=self, window=self._window, notification=notification)

        self.prepend(popup)
        POPUPS.append(popup)

        self._window.visible = True
        popup._outer.reveal_child = True

        utils.Timeout(
            popup._outer.transition_duration, popup._inner.set_reveal_child, True
        )


class NotificationPopup(widgets.Window):
    def __init__(self, monitor: int):
        super().__init__(
            anchor=["right", "top", "bottom"],
            monitor=monitor,
            namespace=f"ignis_NOTIFICATION_POPUP_{monitor}",
            layer="top",
            child=PopupBox(window=self, monitor=monitor),
            visible=False,
            dynamic_input_region=True,
            css_classes=["rec-unset"],
            style="min-width: 29rem;",
        )
