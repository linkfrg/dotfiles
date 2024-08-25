import os
from ignis.utils import Utils

EXPECT_VERSION = ["0", "1"]
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SKIP_DEV_CHECK = os.getenv("SKIP_DEV_CHECK")
SKIP_VER_CHECK = os.getenv("SKIP_VER_CHECK")

BYPASS_DEV_MESSAGE = "To bypass this check set SKIP_DEV_CHECK=1 env var."
BYPASS_VER_MESSAGE = "To bypass this check set SKIP_VER_CHECK=1 env var."


def _check() -> None:
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


def check_version() -> None:
    if SKIP_DEV_CHECK == "1":
        return

    VERSION = Utils.get_ignis_version()
    if os.path.exists(f"{CURRENT_DIR}/.dev"):
        if "dev0" in VERSION:
            _check()
        else:
            print(
                f"ERROR: This branch is supposed to be used with the latest development (git) version of Ignis. {BYPASS_DEV_MESSAGE}"
            )
            exit(1)
    else:
        if "dev0" in VERSION:
            print(
                f"ERROR: You installed the development version of Ignis. To use my dotfiles (main branch), install stable version of Ignis. {BYPASS_DEV_MESSAGE}"
            )
            exit(1)
        else:
            _check()
