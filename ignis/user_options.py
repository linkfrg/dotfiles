import os
from ignis.options_manager import OptionsGroup, OptionsManager
from ignis import CACHE_DIR  # type: ignore


class UserOptions(OptionsManager):
    def __init__(self):
        try:
            super().__init__(file=f"{CACHE_DIR}/user_options.json")
        except FileNotFoundError:
            pass

    class User(OptionsGroup):
        avatar: str = f"/var/lib/AccountsService/icons/{os.getenv('USER')}"

    class Settings(OptionsGroup):
        last_page: int = 0

    class Material(OptionsGroup):
        dark_mode: bool = True
        colors: dict[str, str] = {}

    user = User()
    settings = Settings()
    material = Material()


user_options = UserOptions()
