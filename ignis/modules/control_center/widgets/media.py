import os
import ignis
import asyncio
from ignis import widgets
from ignis.services.mpris import MprisService, MprisPlayer
from ignis import utils
from services.material import MaterialService
from ignis.app import IgnisApp
from ignis.exceptions import StylePathNotFoundError


mpris = MprisService.get_default()
app = IgnisApp.get_default()
material = MaterialService.get_default()

MEDIA_TEMPLATE = utils.get_current_dir() + "/media.scss"
MEDIA_SCSS_CACHE_DIR = ignis.CACHE_DIR + "/media"  # type: ignore
MEDIA_ART_FALLBACK = utils.get_current_dir() + "/../../../misc/media-art-fallback.png"
os.makedirs(MEDIA_SCSS_CACHE_DIR, exist_ok=True)


PLAYER_ICONS = {
    "spotify": "spotify-symbolic",
    "firefox": "firefox-browser-symbolic",
    "chrome": "chrome-symbolic",
    None: "folder-music-symbolic",
}


class Player(widgets.Revealer):
    def __init__(self, player: MprisPlayer) -> None:
        self._player = player
        self._colors_path = f"{MEDIA_SCSS_CACHE_DIR}/{self.clean_desktop_entry()}.scss"
        player.connect("closed", lambda x: self.destroy())
        player.connect("notify::art-url", lambda x, y: self.load_colors())
        self.load_colors()

        super().__init__(
            transition_type="slide_down",
            reveal_child=False,
            css_classes=[self.get_css("media")],
            child=widgets.Overlay(
                child=widgets.Box(css_classes=[self.get_css("media-image")]),
                overlays=[
                    widgets.Box(
                        hexpand=True,
                        vexpand=True,
                        css_classes=[self.get_css("media-image-gradient")],
                    ),
                    widgets.Icon(
                        icon_name=self.get_player_icon(),
                        pixel_size=22,
                        halign="start",
                        valign="start",
                        css_classes=[self.get_css("media-player-icon")],
                    ),
                    widgets.Box(
                        vertical=True,
                        hexpand=True,
                        css_classes=[self.get_css("media-content")],
                        child=[
                            widgets.Box(
                                vexpand=True,
                                valign="center",
                                child=[
                                    widgets.Box(
                                        hexpand=True,
                                        vertical=True,
                                        child=[
                                            widgets.Label(
                                                ellipsize="end",
                                                label=player.bind("title"),
                                                max_width_chars=30,
                                                halign="start",
                                                css_classes=[
                                                    self.get_css("media-title")
                                                ],
                                            ),
                                            widgets.Label(
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
                                    widgets.Button(
                                        child=widgets.Icon(
                                            image=player.bind(
                                                "playback_status",
                                                lambda value: "media-playback-pause-symbolic"
                                                if value == "Playing"
                                                else "media-playback-start-symbolic",
                                            ),
                                            pixel_size=18,
                                        ),
                                        on_click=lambda x: asyncio.create_task(player.play_pause_async()),
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
                    widgets.Box(
                        vexpand=True,
                        valign="end",
                        style="padding: 1rem;",
                        child=[
                            widgets.Scale(
                                value=player.bind("position"),
                                max=player.bind("length"),
                                hexpand=True,
                                css_classes=[self.get_css("media-scale")],
                                on_change=lambda x: asyncio.create_task(self._player.set_position_async(x.value)),
                                visible=player.bind(
                                    "position", lambda value: value != -1
                                ),
                            ),
                            widgets.Button(
                                child=widgets.Icon(
                                    image="media-skip-backward-symbolic",
                                    pixel_size=20,
                                ),
                                css_classes=[self.get_css("media-skip-button")],
                                on_click=lambda x: asyncio.create_task(player.previous_async()),
                                visible=player.bind("can_go_previous"),
                                style="margin-left: 1rem;",
                            ),
                            widgets.Button(
                                child=widgets.Icon(
                                    image="media-skip-forward-symbolic",
                                    pixel_size=20,
                                ),
                                css_classes=[self.get_css("media-skip-button")],
                                on_click=lambda x: asyncio.create_task(player.next_async()),
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
        elif self._player.track_id is not None:
            if "chromium" in self._player.track_id or "chrome" in self._player.track_id:
                return PLAYER_ICONS["chrome"]

        return PLAYER_ICONS[None]

    def destroy(self) -> None:
        self.set_reveal_child(False)
        utils.Timeout(self.transition_duration, super().unparent)

    def get_css(self, class_name: str) -> str:
        return f"{class_name}-{self.clean_desktop_entry()}"

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
        colors["desktop_entry"] = self.clean_desktop_entry()
        material.render_template(
            colors, input_file=MEDIA_TEMPLATE, output_file=self._colors_path
        )
        app.apply_css(self._colors_path)

    def clean_desktop_entry(self) -> str:
        return self._player.desktop_entry.replace(".", "-")


class Media(widgets.Box):
    def __init__(self):
        super().__init__(
            vertical=True,
            setup=lambda self: mpris.connect(
                "player_added", lambda x, player: self.__add_player(player)
            ),
            css_classes=["rec-unset"],
        )

    def __add_player(self, obj: MprisPlayer) -> None:
        player = Player(obj)
        self.append(player)
        player.set_reveal_child(True)
