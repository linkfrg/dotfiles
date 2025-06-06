import asyncio
from ignis import widgets
from ignis.services.notifications import Notification
from ignis import utils


class ScreenshotLayout(widgets.Box):
    def __init__(self, notification: Notification) -> None:
        super().__init__(
            vertical=True,
            hexpand=True,
            child=[
                widgets.Box(
                    child=[
                        widgets.Picture(
                            image=notification.icon,
                            content_fit="cover",
                            width=1920 // 7,
                            height=1080 // 7,
                            style="border-radius: 1rem; background-color: black;",
                        ),
                        widgets.Button(
                            child=widgets.Icon(
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
                widgets.Label(
                    label="Screenshot saved",
                    css_classes=["notification-screenshot-label"],
                ),
                widgets.Box(
                    homogeneous=True,
                    style="margin-top: 0.75rem;",
                    spacing=10,
                    child=[
                        widgets.Button(
                            child=widgets.Label(label="Open"),
                            css_classes=["notification-action"],
                            on_click=lambda x: asyncio.create_task(
                                utils.exec_sh_async(f"xdg-open {notification.icon}")
                            ),
                        ),
                        widgets.Button(
                            child=widgets.Label(label="Close"),
                            css_classes=["notification-action"],
                            on_click=lambda x: notification.close(),
                        ),
                    ],
                ),
            ],
        )


class NormalLayout(widgets.Box):
    def __init__(self, notification: Notification) -> None:
        super().__init__(
            vertical=True,
            hexpand=True,
            child=[
                widgets.Box(
                    child=[
                        widgets.Icon(
                            image=notification.icon
                            if notification.icon
                            else "dialog-information-symbolic",
                            pixel_size=48,
                            halign="start",
                            valign="start",
                        ),
                        widgets.Box(
                            vertical=True,
                            style="margin-left: 0.75rem;",
                            child=[
                                widgets.Label(
                                    ellipsize="end",
                                    label=notification.summary,
                                    halign="start",
                                    visible=notification.summary != "",
                                    css_classes=["notification-summary"],
                                ),
                                widgets.Label(
                                    label=notification.body,
                                    ellipsize="end",
                                    halign="start",
                                    css_classes=["notification-body"],
                                    visible=notification.body != "",
                                ),
                            ],
                        ),
                        widgets.Button(
                            child=widgets.Icon(
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
                widgets.Box(
                    child=[
                        widgets.Button(
                            child=widgets.Label(label=action.label),
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


class NotificationWidget(widgets.Box):
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
