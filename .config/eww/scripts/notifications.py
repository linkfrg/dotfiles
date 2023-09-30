#!/usr/bin/python
import gi
gi.require_version("GdkPixbuf", "2.0")
gi.require_version("Gtk", "3.0")

import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import datetime
import os
import typing
import sys
import json
from gi.repository import Gtk, GdkPixbuf
import subprocess

cache_dir = f"{os.getenv('HOME')}/.cache/notify_img_data"
log_file = f"{os.getenv('HOME')}/.cache/notifications.json"
os.makedirs(cache_dir, exist_ok=True)
active_popups = {}

# RECIEVE NOTIFICATIONS

class NotificationDaemon(dbus.service.Object):
    def __init__(self):
        bus_name = dbus.service.BusName("org.freedesktop.Notifications", dbus.SessionBus())
        dbus.service.Object.__init__(self, bus_name, "/org/freedesktop/Notifications")
        self.notification_id = 0

    @dbus.service.method("org.freedesktop.Notifications", in_signature="susssasa{sv}i", out_signature="u")
    def Notify(self, app_name, replaces_id, app_icon, summary, body, actions, hints, timeout):
        if int(replaces_id) != 0:
            id = int(replaces_id)
        else:
            self.notification_id += 1
            id = self.notification_id
        actions = list(actions)
        acts = []
        for i in range(0, len(actions), 2):
            acts.append([str(actions[i]), str(actions[i + 1])])

        details = {
            "id": id,
            "app": str(app_name),
            "summary": "\n".join([str(summary)[i:i+30] for i in range(0, len(str(summary)), 30)]),
            "body": "\n".join([str(body)[i:i+30] for i in range(0, len(str(body)), 30)]),
            "time": datetime.datetime.now().strftime("%H:%M"),
            "urgency": hints['urgency'],
            "actions": acts
        }

        app_icon = str(app_icon)

        if app_icon.strip():
            if os.path.isfile(app_icon) or app_icon.startswith("file://"):
                details["image"] = app_icon
            else:
                details["image"] = self.get_gtk_icon(app_icon)
        else:
            details["image"] = None

        if "image-data" in hints:
            details["image"] = f"{cache_dir}/{details['id']}.png"
            self.save_img_byte(hints["image-data"], details["image"])

        self.save_notifications(details)
        self.save_popup(details)
        return id

    @dbus.service.method("org.freedesktop.Notifications", in_signature="", out_signature="ssss")
    def GetServerInformation(self):
        return ("linkfrg's notification daemon", "linkfrg", "1.0", "1.2")
    
    @dbus.service.method("org.freedesktop.Notifications", in_signature="", out_signature="as")
    def GetCapabilities(self):
        return ('actions', 'body', 'icon-static', 'persistence')
    
    @dbus.service.method("org.freedesktop.Notifications", in_signature="us", out_signature="us")
    def ActionInvoked(self, id, action):
        return (id, action)
    
    @dbus.service.method("org.freedesktop.Notifications", in_signature="u", out_signature="uu")
    def NotificationClosed(self, id):
        current = self.read_log_file()
        current["notifications"] = [n for n in current["notifications"] if n["id"] != id]
        current["count"] = len(current["notifications"])
        
        self.write_log_file(current)
        return (id, 2)
    

    def get_gtk_icon(self, icon_name):
        theme = Gtk.IconTheme.get_default()
        icon_info = theme.lookup_icon(icon_name, 128, 0)

        if icon_info is not None:
            return icon_info.get_filename()
        

    def save_img_byte(self, px_args: typing.Iterable, save_path: str):
        GdkPixbuf.Pixbuf.new_from_bytes(
            width=px_args[0],
            height=px_args[1],
            has_alpha=px_args[3],
            data=GLib.Bytes(px_args[6]),
            colorspace=GdkPixbuf.Colorspace.RGB,
            rowstride=px_args[2],
            bits_per_sample=px_args[4],
        ).savev(save_path, "png")


    def write_log_file(self, data):
        output_json = json.dumps(data, indent=2)
        subprocess.run(["eww", "update", f"notifications={output_json}"])
        with open(log_file, "w") as log:
            log.write(output_json)

    def read_log_file(self):
        empty = {"count": 0, "notifications": [], "popups": []}
        try:
            with open(log_file, "r") as log:
                return json.load(log)
        except FileNotFoundError:
            with open(log_file, "w") as log:
                json.dump(empty, log)
            return empty
        

    def save_notifications(self, notification):
        current = self.read_log_file()
        current["notifications"].insert(0, notification)
        current["count"] = len(current["notifications"])

        self.write_log_file(current)

    @dbus.service.method("org.freedesktop.Notifications", in_signature="", out_signature="")
    def ClearAll(self):
        data = {"count": 0, "notifications": [], "popups": []}
        
        self.write_log_file(data)


    # OPERATIONS WITH POPUPS

    def save_popup(self, notification):
        global active_popups

        current = self.read_log_file()
        if len(current["popups"]) >= 3:
            oldest_popup = current["popups"].pop()
            self.DismissPopup(oldest_popup["id"])

        current["popups"].insert(0, notification)
        self.write_log_file(current)

        popup_id = notification["id"]
        active_popups[popup_id] = GLib.timeout_add_seconds(5, self.DismissPopup, popup_id)
        os.system('eww open notifications_popup')

    @dbus.service.method("org.freedesktop.Notifications", in_signature="u", out_signature="")
    def DismissPopup(self, id):
        global active_popups

        current = self.read_log_file()
        current["popups"] = [n for n in current["popups"] if n["id"] != id]
        self.write_log_file(current)

        active_popups.pop(id, None)

# MAINLOOP

def main():
    DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()
    daemon = NotificationDaemon()
    data = daemon.read_log_file()
    subprocess.run(["eww", "update", f"notifications={json.dumps(data)}"])
    try:
        loop.run()
    except KeyboardInterrupt:
        exit(0)

if __name__ == "__main__":
    main()
