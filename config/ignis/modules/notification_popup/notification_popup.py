from gi.repository import IgnisNotificationsGLib
from ignis import utils, widgets
from ignis.window_manager import WindowManager
from setup import get_notification_service

from ..shared_widgets import NotificationWidget

service = get_notification_service()

window_manager = WindowManager.get_default()


class Popup(widgets.Box):
    def __init__(
        self,
        notification: IgnisNotificationsGLib.Notification,
    ):
        self._destroyed = False

        widget = NotificationWidget(notification)
        widget.css_classes = ["notification-popup"]

        self.inner = widgets.Revealer(transition_type="slide_left", child=widget)
        self.outer = widgets.Revealer(transition_type="slide_down", child=self.inner)

        super().__init__(child=[self.outer], halign="end")


class PopupBox(widgets.Box):
    def __init__(self, window: "NotificationPopup", monitor: int):
        self._window = window
        self._monitor = monitor
        self._popups = []

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
        popup = Popup(notification=notification)

        self.prepend(popup)
        self._popups.append(popup)

        self._window.visible = True
        popup.outer.reveal_child = True

        notification.connect(
            "closed", lambda x, reason, popup=popup: self.destroy_popup(popup)
        )

        utils.Timeout(3000, lambda popup=popup: self.destroy_popup(popup))

        utils.Timeout(
            popup.outer.transition_duration, popup.inner.set_reveal_child, True
        )

    def destroy_popup(self, popup):
        def box_destroy():
            popup.unparent()
            self._popups.remove(popup)

            if len(self._popups) == 0:
                self._window.visible = False

        def outer_close():
            popup.outer.reveal_child = False
            utils.Timeout(popup.outer.transition_duration, box_destroy)

        if popup._destroyed:
            return
        else:
            popup._destroyed = True

        popup.inner.transition_type = "crossfade"
        popup.inner.reveal_child = False

        utils.Timeout(popup.outer.transition_duration, outer_close)


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
