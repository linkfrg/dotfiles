from ignis.widgets import Widget
from ignis.services import Service
from ignis.services.mpris import MprisService, MprisPlayer
from ignis.utils import Utils

mpris: MprisService = Service.get("mpris")


def format_seconds(seconds: int) -> str:
    if seconds:
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes}:{seconds:02d}"


class Player(Widget.Revealer):
    def __init__(self, player: MprisPlayer) -> None:
        super().__init__(
            transition_type="crossfade",
            reveal_child=False,
            child=Widget.Box(
                css_classes=["media"],
                vertical=True,
                hexpand=True,
                child=[
                    Widget.Box(
                        child=[
                            Widget.Picture(
                                image=player.bind("art_url"),
                                width=56,
                                height=56,
                                style="border-radius: 0.5rem;",
                                content_fit="cover",
                            ),
                            Widget.Box(
                                hexpand=True,
                                vertical=True,
                                valign="center",
                                style="margin-left: 1rem;",
                                child=[
                                    Widget.Label(
                                        ellipsize="end",
                                        label=player.bind("title"),
                                        max_width_chars=25,
                                        halign="start",
                                    ),
                                    Widget.Label(
                                        label=player.bind("artist"),
                                        max_width_chars=25,
                                        halign="start",
                                        css_classes=["media-artist"],
                                    ),
                                ],
                            ),
                        ]
                    ),
                    Widget.Box(
                        style="margin-top: 0.5rem;",
                        visible=player.bind("position", lambda value: value != -1),
                        child=[
                            Widget.Scale(
                                value=player.bind("position"),
                                max=player.bind("length"),
                                hexpand=True,
                                css_classes=["media-scale"],
                                on_change=lambda x: player.set_position(x.value),
                            )
                        ],
                    ),
                    Widget.Box(
                        style="margin-top: 0.25rem;",
                        visible=player.bind("position", lambda value: value != -1),
                        child=[
                            Widget.Label(
                                label=player.bind(
                                    "position",
                                    lambda value: format_seconds(value),
                                ),
                            ),
                            Widget.Label(
                                label=player.bind(
                                    "length", lambda value: format_seconds(value)
                                ),
                                halign="end",
                                hexpand=True,
                            ),
                        ],
                    ),
                    Widget.Box(
                        halign="center",
                        child=[
                            Widget.Button(
                                child=Widget.Icon(
                                    image="media-skip-backward-symbolic",
                                    pixel_size=20,
                                ),
                                on_click=lambda x: player.previous(),
                                visible=player.bind("can_go_previous"),
                                css_classes=["media-button"],
                            ),
                            Widget.Button(
                                child=Widget.Icon(
                                    image=player.bind(
                                        "playback_status",
                                        lambda value: "media-playback-pause-symbolic"
                                        if value == "Playing"
                                        else "media-playback-start-symbolic",
                                    ),
                                    pixel_size=20,
                                ),
                                on_click=lambda x: player.play_pause(),
                                visible=player.bind("can_play"),
                                css_classes=["media-button"],
                            ),
                            Widget.Button(
                                child=Widget.Icon(
                                    image="media-skip-forward-symbolic",
                                    pixel_size=20,
                                ),
                                on_click=lambda x: player.next(),
                                visible=player.bind("can_go_next"),
                                css_classes=["media-button"],
                            ),
                        ],
                    ),
                ],
            ),
        )
        player.connect("closed", lambda x: self.destroy())

    def destroy(self) -> None:
        self.set_reveal_child(False)
        Utils.Timeout(self.transition_duration, super().unparent)


def media() -> Widget.Box:
    def add_player(box: Widget.Box, obj: MprisPlayer) -> None:
        player = Player(obj)
        box.append(player)
        player.set_reveal_child(True)

    return Widget.Box(
        vertical=True,
        setup=lambda self: mpris.connect(
            "player_added", lambda x, player: add_player(self, player)
        ),
        css_classes=["rec-unset"],
    )
