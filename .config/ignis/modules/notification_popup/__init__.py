from ignis.widgets import Widget
from ignis.app import app
from ignis.utils import Utils
from ignis.services import Service
from ignis.services.notifications import Notification, NotificationService

notifications: NotificationService = Service.get("notifications")


class NotificationWidget(Widget.Box):
    def __init__(self, notification: Notification) -> None:
        if notification.app_name == "grimblast":
            layout = [
                Widget.Picture(
                    image=notification.icon,
                    content_fit="cover",
                    width=1920 / 6,
                    height=1080 / 6,
                ),
            ]
        else:
            layout = [
                Widget.Box(
                    child=[
                        Widget.Icon(
                            image=notification.icon
                            if notification.icon
                            else "dialog-information-symbolic",
                            pixel_size=48,
                            halign="start",
                            valign="start",
                        ),
                        Widget.Box(
                            vertical=True,
                            child=[
                                Widget.Label(
                                    ellipsize="end",
                                    label=notification.summary,
                                    halign="start",
                                    visible=notification.summary != "",
                                ),
                                Widget.Label(
                                    label=notification.body,
                                    ellipsize="end",
                                    halign="start",
                                    css_classes=["notification-body"],
                                    visible=notification.body != "",
                                ),
                            ],
                            style="margin-left: 0.75rem;",
                        ),
                        Widget.Button(
                            child=Widget.Icon(
                                image="window-close-symbolic", pixel_size=20
                            ),
                            halign="end",
                            valign="start",
                            hexpand=True,
                            css_classes=["notification-close"],
                            on_click=lambda x: notification.dismiss(),
                        ),
                    ],
                ),
                Widget.Box(
                    child=[
                        Widget.Button(
                            child=Widget.Label(label=action.label),
                            on_click=lambda x, action=action: action.invoke(),
                            css_classes=["notification-action"],
                        )
                        for action in notification.actions
                    ],
                    style="margin-top: 0.5rem;" if notification.actions else "",
                    spacing=10,
                ),
            ]

        super().__init__(
            css_classes=["notification-popup"],
            vertical=True,
            style="min-width: 0rem;" if notification.app_name == "grimblast" else "",
            child=layout,
        )


class Popup(Widget.Box):
    def __init__(self, notification: Notification):
        widget = NotificationWidget(notification)
        self._inner = Widget.Revealer(transition_type="slide_left", child=widget)
        self._outer = Widget.Revealer(transition_type="slide_down", child=self._inner)
        super().__init__(child=[self._outer], halign="end")

        notification.connect("dismissed", lambda x: self.destroy())

    def destroy(self):
        def box_destroy():
            box = self.get_parent()
            self.unparent()
            if len(notifications.popups) == 0:
                window = box.get_parent()
                window.visible = False
            else:
                change_window_input_region(box)

        def outer_close():
            self._outer.reveal_child = False
            Utils.Timeout(self._outer.transition_duration, box_destroy)

        self._inner.transition_type = "crossfade"
        self._inner.reveal_child = False
        Utils.Timeout(self._outer.transition_duration, outer_close)


def on_notified(box: Widget.Box, notification: Notification, monitor: int) -> None:
    app.open_window(f"ignis_NOTIFICATION_POPUP_{monitor}")
    popup = Popup(notification)
    box.prepend(popup)
    popup._outer.reveal_child = True
    Utils.Timeout(popup._outer.transition_duration, reveal_popup, box, popup)


def reveal_popup(box: Widget.Box, popup: Popup) -> None:
    popup._inner.set_reveal_child(True)
    change_window_input_region(box)


def change_window_input_region(box: Widget.Box) -> None:
    width = box.get_width()
    height = box.get_height()
    window = box.get_parent()
    window.input_width = width
    window.input_height = height


def notification_popup(monitor: int) -> Widget.Window:
    notifications_box = Widget.Box(
        vertical=True,
        valign="start",
        setup=lambda self: notifications.connect(
            "new_popup",
            lambda x, notification: on_notified(
                notifications_box, notification, monitor
            ),
        ),
    )

    return Widget.Window(
        anchor=["right", "top", "bottom"],
        monitor=monitor,
        namespace=f"ignis_NOTIFICATION_POPUP_{monitor}",
        layer="top",
        child=notifications_box,
        visible=False,
        css_classes=["rec-unset"],
        style="min-width: 29rem;",
    )
