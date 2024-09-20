import os
import ignis
from ignis.widgets import Widget
from ignis.services.mpris import MprisService, MprisPlayer
from ignis.utils import Utils
from services.material import MaterialService
from ignis.app import IgnisApp
from ignis.exceptions import StylePathNotFoundError


mpris = MprisService.get_default()
app = IgnisApp.get_default()
material = MaterialService.get_default()

MEDIA_TEMPLATE = Utils.get_current_dir() + "/../../scss/media.scss"
MEDIA_SCSS_CACHE_DIR = ignis.CACHE_DIR + "/media"  # type: ignore
MEDIA_ART_FALLBACK = Utils.get_current_dir() + "/../../misc/media-art-fallback.png"
os.makedirs(MEDIA_SCSS_CACHE_DIR, exist_ok=True)


PLAYER_ICONS = {"spotify": "󰓇", "firefox": "󰈹", "chrome": "󰊯", None: ""}


class Player(Widget.Revealer):
    def __init__(self, player: MprisPlayer) -> None:
        self._player = player
        self._colors_path = f"{MEDIA_SCSS_CACHE_DIR}/{self._player.desktop_entry}.scss"
        player.connect("closed", lambda x: self.destroy())
        player.connect("notify::art-url", lambda x, y: self.load_colors())
        self.load_colors()

        super().__init__(
            transition_type="slide_down",
            reveal_child=False,
            css_classes=[self.get_css("media")],
            child=Widget.Overlay(
                child=Widget.Box(css_classes=[self.get_css("media-image")]),
                overlays=[
                    Widget.Box(
                        hexpand=True,
                        vexpand=True,
                        css_classes=[self.get_css("media-image-gradient")],
                    ),
                    Widget.Label(
                        label=self.get_player_icon(),
                        halign="start",
                        valign="start",
                        css_classes=[self.get_css("media-player-icon")],
                    ),
                    Widget.Box(
                        vertical=True,
                        hexpand=True,
                        css_classes=[self.get_css("media-content")],
                        child=[
                            Widget.Box(
                                vexpand=True,
                                valign="center",
                                child=[
                                    Widget.Box(
                                        hexpand=True,
                                        vertical=True,
                                        child=[
                                            Widget.Label(
                                                ellipsize="end",
                                                label=player.bind("title"),
                                                max_width_chars=30,
                                                halign="start",
                                                css_classes=[
                                                    self.get_css("media-title")
                                                ],
                                            ),
                                            Widget.Label(
                                                label=player.bind("artist"),
                                                max_width_chars=30,
                                                ellipsize="end",
                                                halign="start",
                                                css_classes=[
                                                    self.get_css("media-artist")
                                                ],
                                            ),
                                        ],
                                    ),
                                    Widget.Button(
                                        child=Widget.Icon(
                                            image=player.bind(
                                                "playback_status",
                                                lambda value: "media-playback-pause-symbolic"
                                                if value == "Playing"
                                                else "media-playback-start-symbolic",
                                            ),
                                            pixel_size=18,
                                        ),
                                        on_click=lambda x: player.play_pause(),
                                        visible=player.bind("can_play"),
                                        css_classes=player.bind(
                                            "playback_status",
                                            lambda value: [
                                                self.get_css("media-playback-button"),
                                                "playing",
                                            ]
                                            if value == "Playing"
                                            else [
                                                self.get_css("media-playback-button"),
                                                "paused",
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                    Widget.Box(
                        vexpand=True,
                        valign="end",
                        style="padding: 1rem;",
                        child=[
                            Widget.Scale(
                                value=player.bind("position"),
                                max=player.bind("length"),
                                hexpand=True,
                                css_classes=[self.get_css("media-scale")],
                                on_change=lambda x: player.set_position(x.value),
                                visible=player.bind(
                                    "position", lambda value: value != -1
                                ),
                            ),
                            Widget.Button(
                                child=Widget.Icon(
                                    image="media-skip-backward-symbolic",
                                    pixel_size=20,
                                ),
                                css_classes=[self.get_css("media-skip-button")],
                                on_click=lambda x: player.previous(),
                                visible=player.bind("can_go_previous"),
                                style="margin-left: 1rem;",
                            ),
                            Widget.Button(
                                child=Widget.Icon(
                                    image="media-skip-forward-symbolic",
                                    pixel_size=20,
                                ),
                                css_classes=[self.get_css("media-skip-button")],
                                on_click=lambda x: player.next(),
                                visible=player.bind("can_go_next"),
                                style="margin-left: 1rem;",
                            ),
                        ],
                    ),
                ],
            ),
        )

    def get_player_icon(self) -> str:
        if self._player.desktop_entry == "firefox":
            return PLAYER_ICONS["firefox"]
        elif self._player.desktop_entry == "spotify":
            return PLAYER_ICONS["spotify"]
        elif "chromium" in self._player.track_id or "chrome" in self._player.track_id:
            return PLAYER_ICONS["chrome"]
        else:
            return PLAYER_ICONS[None]

    def destroy(self) -> None:
        self.set_reveal_child(False)
        Utils.Timeout(self.transition_duration, super().unparent)

    def get_css(self, class_name: str) -> str:
        return f"{class_name}-{self._player.desktop_entry}"

    def load_colors(self) -> None:
        if not self._player.art_url:
            art_url = MEDIA_ART_FALLBACK
        else:
            art_url = self._player.art_url

        try:
            app.remove_css(self._colors_path)
        except StylePathNotFoundError:
            pass

        colors = material.get_colors_from_img(art_url, True)
        colors["art_url"] = art_url
        colors["desktop_entry"] = self._player.desktop_entry
        material.render_template(
            colors, input_file=MEDIA_TEMPLATE, output_file=self._colors_path
        )
        app.apply_css(self._colors_path)


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
