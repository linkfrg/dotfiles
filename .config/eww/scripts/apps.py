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
            continue

        app_name = parser.get("Desktop Entry", "Name")
        icon_path = get_gtk_icon(parser.get("Desktop Entry", "Icon", fallback=None))

        entry = {
            "name": app_name,
            "icon": icon_path,
            "desktop": os.path.basename(file_path),
        }
        entries.append(entry)

    

    return {"apps": entries, "pinned": read_cache(), "search": False, "filtered": []}



def write_cache(entries):
    with open(CACHE_FILE, "w") as file:
        json.dump(entries, file, indent=2)

def read_cache():
    empty = []
    try:
        with open(CACHE_FILE, "r") as cache:
            return json.load(cache)
    except FileNotFoundError:
        with open(CACHE_FILE, "w") as cache:
            json.dump(empty, cache)
        return empty

def filter_entries(entries, query):
    filtered_data = [
        entry for entry in entries["apps"]
        if query.lower() in entry["name"].lower()
    ]
    return filtered_data

def update_eww(entries):
    subprocess.run(["eww", "update", f"apps={json.dumps(entries)}"])


def add_pinned_entry(name, icon, desktop):
    entry = {
            "name": name,
            "icon": icon,
            "desktop": desktop,
        }
    cache = read_cache()
    for c in cache:
        if c['desktop'] == desktop:
            print("App already pinned!")
            exit(1)

    cache.insert(0, entry)
    write_cache(cache)

    update_eww(get_desktop_entries())


def remove_pinned_entry(desktop):
    cache = read_cache()
    pins = [entry for entry in cache if entry['desktop'] != desktop]
    write_cache(pins)

    update_eww(get_desktop_entries())
    

if __name__ == "__main__":
    if len(sys.argv) > 2:
        if sys.argv[1] == "--query":
            query = sys.argv[2]
            if query == "":
                entries = get_desktop_entries()
                update_eww(entries)
                exit(0)
            entries = get_desktop_entries()
            filtered = filter_entries(entries, query)
            update_eww({"apps": entries['apps'], "pinned": entries['pinned'], "search": True, "filtered": filtered})

        elif sys.argv[1] == "--add-pin":
            name = sys.argv[2]
            icon = sys.argv[3]
            desktop = sys.argv[4]
            add_pinned_entry(name, icon, desktop)

        elif sys.argv[1] == "--remove-pin":
            desktop = sys.argv[2]
            remove_pinned_entry(desktop)
    else:
        entries = get_desktop_entries()
        update_eww(entries)

    