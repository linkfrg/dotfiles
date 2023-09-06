#!/usr/bin/python

import glob
import sys
import os
import json
import subprocess
import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from configparser import ConfigParser

CACHE_FILE = os.path.expanduser("~/.cache/apps.json")
DESKTOP_DIR = "/usr/share/applications"
PREFERRED_APPS = [
    "firefox web browser",
    "visual studio code",
    "telegram desktop"
]

def get_gtk_icon(icon_name):
    theme = Gtk.IconTheme.get_default()
    icon_info = theme.lookup_icon(icon_name, 128, 0)

    if icon_info is not None:
        return icon_info.get_filename()

def get_desktop_entries():
    desktop_files = glob.glob(os.path.join(DESKTOP_DIR, "*.desktop"))
    entries = []

    for file_path in desktop_files:
        parser = ConfigParser()
        parser.read(file_path)

        if parser.getboolean("Desktop Entry", "NoDisplay", fallback=False):
            continue  # Skip entries with NoDisplay=true

        app_name = parser.get("Desktop Entry", "Name")
        icon_path = get_gtk_icon(parser.get("Desktop Entry", "Icon", fallback=None))
        comment = parser.get("Desktop Entry", "Comment", fallback=None)

        entry = {
            "name": app_name,
            "icon": icon_path,
            "comment": comment,
            "desktop": os.path.basename(file_path),
        }
        entries.append(entry)
    return entries

def update_cache(all_apps, preferred_apps):
    data = {"apps": all_apps, "preferred": preferred_apps}
    with open(CACHE_FILE, "w") as file:
        json.dump(data, file, indent=2)

def get_cached_entries():
    all_apps = get_desktop_entries()
    preferred_apps = [entry for entry in all_apps if entry["name"].lower() in PREFERRED_APPS]
    update_cache(all_apps, preferred_apps)
    return {"apps": all_apps, "preferred": preferred_apps}

def filter_entries(entries, query):
    filtered_data = [
        entry for entry in entries["apps"]
        if query.lower() in entry["name"].lower()
        or (entry["comment"] and query.lower() in entry["comment"].lower())
    ]
    return filtered_data

def update_eww(entries):
    subprocess.run(["eww", "update", "apps={}".format(json.dumps(entries))])

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--query":
        query = sys.argv[2]
    else:
        query = None

    entries = get_cached_entries()

    if query is not None:
        filtered = filter_entries(entries, query)
        update_eww({"apps": filtered, "preferred": entries["preferred"]})
    else:
        update_eww(entries)