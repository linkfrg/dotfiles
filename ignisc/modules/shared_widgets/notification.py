import asyncio
from ignis.widgets import Widget
from ignis.services.notifications import Notification
from ignis.utils import Utils


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
                            on_click=lambda x: asyncio.create_task(
                                Utils.exec_sh_async(f"xdg-open {notification.icon}")
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
