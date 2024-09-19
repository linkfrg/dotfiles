import os
from ignis.services.options import OptionsService

options = OptionsService.get_default()

USER_OPT_GROUP = options.create_group("user", exists_ok=True)
USER_OPT_GROUP.create_option(
    "avatar",
    default=f"/var/lib/AccountsService/icons/{os.getenv('USER')}",
    exists_ok=True,
)

SETTINGS_OPT_GROUP = options.create_group("settings", exists_ok=True)
SETTINGS_OPT_GROUP.create_option(
    "last_page",
    default=0,
    exists_ok=True,
)
