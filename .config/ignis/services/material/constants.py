import os
import ignis
from ignis.utils import Utils


MATERIAL_CACHE_DIR = f"{ignis.CACHE_DIR}/material"  # type: ignore

TEMPLATES = Utils.get_current_dir() + "/templates"
SAMPLE_WALL = Utils.get_current_dir() + "/sample_wall.png"

SWAYLOCK_CONFIG_DIR = os.path.expanduser("~/.config/swaylock")
SWAYLOCK_CONFIG = f"{SWAYLOCK_CONFIG_DIR}/config"

os.makedirs(MATERIAL_CACHE_DIR, exist_ok=True)
os.makedirs(SWAYLOCK_CONFIG_DIR, exist_ok=True)
