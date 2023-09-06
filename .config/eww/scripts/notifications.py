#!/usr/bin/python

import gi
import datetime
import typing
import os
import json
import sys
import subprocess
gi.require_version("GdkPixbuf", "2.0")
gi.require_version("Gtk", "3.0")

import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GdkPixbuf, Gio, GLib, Gtk

cache_dir = os.path.expanduser("~/.cache/image_data")
log_file = os.path.expanduser("~/.cache/notifications.json")
os.makedirs(cache_dir, exist_ok=True)
active_popups = {}

def save_img_byte(px_args: typing.Iterable, save_path: str):
    GdkPixbuf.Pixbuf.new_from_bytes(
        width=px_args[0],
        height=px_args[1],
        has_alpha=px_args[3],
        data=GLib.Bytes(px_args[6]),
        colorspace=GdkPixbuf.Colorspace.RGB,
        rowstride=px_args[2],
        bits_per_sample=px_args[4],
    ).savev(save_path, "png")

def get_gtk_icon(icon_name):
    theme = Gtk.IconTheme.get_default()
    icon_info = theme.lookup_icon(icon_name, 128, 0)

    if icon_info is not None:
        return icon_info.get_filename()



def notification_callback(bus, message):
    args = message.get_args_list()
    details = {
        "id": datetime.datetime.now().strftime("%s"),
        "app": str(args[0]) or None,
        "summary": str(args[3]) or None,
        "body": str(args[4]) or None,
        "time": datetime.datetime.now().strftime("%H:%M"),
    }

    if args[2].strip():
        if os.path.isfile(args[2]) or args[2].startswith("file://"):
            details["image"] = args[2]
        else:
            details["image"] = get_gtk_icon(args[2])
    else:
        details["image"] = None

    if "image-data" in args[6]:
        details["image"] = f"{cache_dir}/{details['id']}.png"
        save_img_byte(args[6]["image-data"], details["image"])
    
    save_notifications(details)
    save_popup(details)

def update_eww(data):
    output_json = json.dumps(data, indent=2)
    subprocess.run(["eww", "update", f"notifications={output_json}"])
    with open(log_file, "w") as log:
        log.write(output_json)

def read_log_file():
    empty = {"count": 0, "notifications": [], "popups": []}
    try:
        with open(log_file, "r") as log:
            return json.load(log)
    except FileNotFoundError:
        with open(log_file, "w") as log:
            json.dump(empty, log)
        return empty

def save_notifications(notification):
    current = read_log_file()
    current["notifications"].insert(0, notification)
    current["count"] = len(current["notifications"])

    update_eww(current)

def clear_notifications():
    data = {"count": 0, "notifications": [], "popups": []}
    
    update_eww(data)


def remove_notification(id):
    current = read_log_file()
    current["notifications"] = [n for n in current["notifications"] if n["id"] != id]
    current["count"] = len(current["notifications"])
    
    update_eww(current)

def save_popup(notification):
    global active_popups

    current = read_log_file()
    if len(current["popups"]) >= 3:
        oldest_popup = current["popups"].pop()
        remove_notification(oldest_popup["id"])

    current["popups"].insert(0, notification)
    update_eww(current)

    popup_id = notification["id"]
    active_popups[popup_id] = GLib.timeout_add_seconds(5, remove_popup, popup_id)
    os.system('eww open notifications_popup')

def remove_popup(popup_id):
    global active_popups

    current = read_log_file()
    current["popups"] = [n for n in current["popups"] if n["id"] != popup_id]
    update_eww(current)

    active_popups.pop(popup_id, None)

def notification_loop():
    DBusGMainLoop(set_as_default=True)

    bus = dbus.SessionBus()
    bus.add_match_string_non_blocking(
        "eavesdrop=true, interface='org.freedesktop.Notifications', member='Notify'"
    )

    bus.add_message_filter(notification_callback)

    loop = GLib.MainLoop()
    try:
        loop.run()
    except KeyboardInterrupt:
        bus.close()

if __name__ == "__main__":
    arg = sys.argv[1]
    if arg == "init":
        notification_loop()
    elif arg == "clear":
        clear_notifications()
    elif arg == "remove_popup":
        remove_popup(sys.argv[2])