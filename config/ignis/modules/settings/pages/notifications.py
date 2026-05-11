from ..elements import SwitchRow, SettingsPage, SettingsGroup, SpinRow, SettingsEntry
from ignis.options import options


class NotificationsEntry(SettingsEntry):
    def __init__(self):
        page = SettingsPage(
            name="Notifications",
            groups=[
                SettingsGroup(
                    name="General",
                    rows=[
                        SwitchRow(
                            label="Do not disturb",
                            active=options.notifications.bind("dnd"),
                            on_change=lambda x, state: options.notifications.set_dnd(
                                state
                            ),
                        ),
                        SpinRow(
                            label="Maximum popups count",
                            sublabel="The first popup will automatically dismiss",
                            value=options.notifications.bind("max_popups_count"),
                            min=1,
                            on_change=lambda x,
                            value: options.notifications.set_max_popups_count(value),
                        ),
                        SpinRow(
                            label="Popup timeout",
                            sublabel="Timeout before popup will be dismissed, in milliseconds.",
                            max=100000,
                            step=100,
                            value=options.notifications.bind("popup_timeout"),
                            on_change=lambda x,
                            value: options.notifications.set_popup_timeout(value),
                        ),
                    ],
                )
            ],
        )
        super().__init__(
            label="Notifications",
            icon="notification-symbolic",
            page=page,
        )
