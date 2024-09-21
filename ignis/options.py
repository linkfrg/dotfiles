import os
from ignis.services.options import OptionsService

options = OptionsService.get_default()

user_opt_group = options.create_group("user", exists_ok=True)
avatar_opt = user_opt_group.create_option(
    "avatar",
    default=f"/var/lib/AccountsService/icons/{os.getenv('USER')}",
    exists_ok=True,
)

settings_opt_group = options.create_group("settings", exists_ok=True)
settings_last_page = settings_opt_group.create_option(
    "last_page",
    default=0,
    exists_ok=True,
)
