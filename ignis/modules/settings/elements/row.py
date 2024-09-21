from ignis.widgets import Widget


class SettingsRow(Widget.ListBoxRow):
    def __init__(self, label: str | None = None, sublabel: str | None = None, **kwargs):
        super().__init__(
            css_classes=["settings-row"],
            child=Widget.Box(
                child=[
                    Widget.Box(
                        vertical=True,
                        child=[
                            Widget.Label(
                                label=label,
                                css_classes=["settings-row-label"],
                                halign="start",
                                vexpand=True,
                                wrap=True,
                                visible=True if label else False,
                            ),
                            Widget.Label(
                                label=sublabel,
                                css_classes=["settings-row-sublabel"],
                                halign="start",
                                vexpand=True,
                                wrap=True,
                                visible=True if sublabel else False,
                            ),
                        ],
                    )
                ]
            ),
            **kwargs,
        )
