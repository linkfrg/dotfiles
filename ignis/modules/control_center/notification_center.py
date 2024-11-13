from ignis.widgets import Widget
from ignis.services.notifications import Notification, NotificationService
from ignis.utils import Utils
from gi.repository import GLib  # type: ignore

notifications = NotificationService.get_default()


class ScreenshotLayout(Widget.Box):
    def __init__(self, notification: Notification) -> None:
        super().__init__(
            vertical=True,
            hexpand=True,
            child=[
                Widget.Box(
                    child=[
                        Widget.Picture(
                            image=notification.icon,
                            content_fit="cover",
                            width=1920 // 7,
                            height=1080 // 7,
                            style="border-radius: 1rem; background-color: black;",
                        ),
                        Widget.Button(
                            child=Widget.Icon(
                                image="window-close-symbolic", pixel_size=20
                            ),
                            halign="end",
                            valign="start",
                            hexpand=True,
                            css_classes=["notification-close"],
                            on_click=lambda x: notification.close(),
                        ),
                    ],
                ),
                Widget.Label(
                    label="Screenshot saved",
                    css_classes=["notification-screenshot-label"],
                ),
                Widget.Box(
                    homogeneous=True,
                    style="margin-top: 0.75rem;",
                    spacing=10,
                    child=[
                        Widget.Button(
                            child=Widget.Label(label="Open"),
                            css_classes=["notification-action"],
                            on_click=lambda x: Utils.exec_sh_async(
                                f"xdg-open {notification.icon}"
                            ),
                        ),
                        Widget.Button(
                            child=Widget.Label(label="Close"),
                            css_classes=["notification-action"],
                            on_click=lambda x: notification.close(),
                        ),
                    ],
                ),
            ],
        )


class NormalLayout(Widget.Box):
    def __init__(self, notification: Notification) -> None:
        super().__init__(
            vertical=True,
            hexpand=True,
            child=[
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
                            style="margin-left: 0.75rem;",
                            child=[
                                Widget.Label(
                                    ellipsize="end",
                                    label=notification.summary,
                                    halign="start",
                                    visible=notification.summary != "",
                                    css_classes=["notification-summary"],
                                ),
                                Widget.Label(
                                    label=notification.body,
                                    ellipsize="end",
                                    halign="start",
                                    css_classes=["notification-body"],
                                    visible=notification.body != "",
                                ),
                            ],
                        ),
                        Widget.Button(
                            child=Widget.Icon(
                                image="window-close-symbolic", pixel_size=20
                            ),
                            halign="end",
                            valign="start",
                            hexpand=True,
                            css_classes=["notification-close"],
                            on_click=lambda x: notification.close(),
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
                    homogeneous=True,
                    style="margin-top: 0.75rem;" if notification.actions else "",
                    spacing=10,
                ),
            ],
        )


class NotificationWidget(Widget.Box):
    def __init__(self, notification: Notification) -> None:
        layout: NormalLayout | ScreenshotLayout

        if notification.app_name == "grimblast":
            layout = ScreenshotLayout(notification)
        else:
            layout = NormalLayout(notification)

        super().__init__(
            css_classes=["notification"],
            child=[layout],
        )


class Popup(Widget.Revealer):
    def __init__(self, notification: Notification, **kwargs):
        widget = NotificationWidget(notification)
        super().__init__(child=widget, transition_type="slide_down", **kwargs)

        notification.connect("closed", lambda x: self.destroy())

    def destroy(self):
        self.reveal_child = False
        Utils.Timeout(self.transition_duration, self.unparent)


def loading_notif_label() -> Widget.Label:
    return Widget.Label(
        label="Loading notifications...",
        valign="center",
        vexpand=True,
        css_classes=["notification-center-info-label"],
    )


def no_notifications_label() -> Widget.Label:
    return Widget.Label(
        label="No notifications",
        valign="center",
        vexpand=True,
        visible=notifications.bind("notifications", lambda value: len(value) == 0),
        css_classes=["notification-center-info-label"],
    )


def on_notified(box: Widget.Box, notification: Notification) -> None:
    notify = Popup(notification)
    box.prepend(notify)
    notify.reveal_child = True


def load_notifications() -> list[Widget.Label | Popup]:
    widgets = []
    for i in notifications.notifications:
        GLib.idle_add(lambda i=i: widgets.append(Popup(i, reveal_child=True)))
    return widgets


def notification_list() -> Widget.Box:
    box = Widget.Box(
        vertical=True,
        child=[loading_notif_label()],
        vexpand=True,
        css_classes=["rec-unset"],
        setup=lambda self: notifications.connect(
            "notified",
            lambda x, notification: on_notified(self, notification),
        ),
    )

    Utils.ThreadTask(
        load_notifications,
        lambda result: box.set_child(result + [no_notifications_label()]),
    ).run()

    return box


def notification_center() -> Widget.Box:
    main_box = Widget.Box(
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
                child=notification_list(),
                vexpand=True,
            ),
        ],
    )

    return main_box
