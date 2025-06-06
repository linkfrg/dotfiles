import os
import ignis
from ignis import utils


MATERIAL_CACHE_DIR = f"{ignis.CACHE_DIR}/material"  # type: ignore

TEMPLATES = utils.get_current_dir() + "/templates"
SAMPLE_WALL = utils.get_current_dir() + "/sample_wall.png"

os.makedirs(MATERIAL_CACHE_DIR, exist_ok=True)
