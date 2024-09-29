import os
from ignis.utils import Utils

EXPECT_VERSION = ["0", "2"]

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

SKIP_VER_CHECK = os.getenv("SKIP_VER_CHECK")
BYPASS_VER_MESSAGE = "To bypass this check set SKIP_VER_CHECK=1 env var."

def check_version() -> None:
    if SKIP_VER_CHECK == "1":
        return

    VERSION = Utils.get_ignis_version().replace("dev0", "").split(".")

    if int(VERSION[0]) < int(EXPECT_VERSION[0]) or int(VERSION[1]) < int(
        EXPECT_VERSION[1]
    ):
        print(
            f"ERROR: My dotfiles requires at least Ignis v{'.'.join(EXPECT_VERSION)}, current version: v{'.'.join(VERSION)}. {BYPASS_VER_MESSAGE}"
        )
        exit(1)
