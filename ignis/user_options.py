import os
from ignis.options_manager import OptionsGroup, OptionsManager
from ignis import DATA_DIR, CACHE_DIR  # type: ignore

USER_OPTIONS_FILE = f"{DATA_DIR}/user_options.json"
OLD_USER_OPTIONS_FILE = f"{CACHE_DIR}/user_options.json"


# FIXME: remove someday
def _migrate_old_options_file() -> None:
    with open(OLD_USER_OPTIONS_FILE) as f:
        data = f.read()

    with open(USER_OPTIONS_FILE, "w") as f:
        f.write(data)


class UserOptions(OptionsManager):
    def __init__(self):
        if not os.path.exists(USER_OPTIONS_FILE) and os.path.exists(
            OLD_USER_OPTIONS_FILE
        ):
            _migrate_old_options_file()

        try:
            super().__init__(file=USER_OPTIONS_FILE)
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
