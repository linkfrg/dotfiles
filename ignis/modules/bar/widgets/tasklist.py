#!/usr/bin/env python3
import os
import re
import subprocess
import json
from pathlib import Path
from threading import Thread
from ignis import widgets
from ignis.app import IgnisApp
from ignis.services.hyprland import HyprlandService, HyprlandWorkspace

hyprland = HyprlandService.get_default()
ignis_app = IgnisApp.get_default()


def is_main_desktop_file(desktop_file):
    name = desktop_file.stem.lower()
    return not any(x in name for x in ['url-handler', 'handler', 'wayland', 'wrapper'])

def find_best_desktop_match(search_term):
    desktop_dirs = [
        Path("/usr/share/applications/"),
        Path.home() / ".local/share/applications/"
    ]
    
    all_matches = []
    for desktop_dir in desktop_dirs:
        if not desktop_dir.exists():
            continue
            
        for desktop_file in desktop_dir.glob("*.desktop"):
            try:
                content = desktop_file.read_text()
                if (f"Exec={search_term}" in content or 
                    f"StartupWMClass={search_term}" in content or
                    search_term.lower() in desktop_file.stem.lower()):
                    
                    info = {
                        "path": str(desktop_file),
                        "is_main": is_main_desktop_file(desktop_file),
                        "score": 0
                    }
                    
                    # Score matches (higher is better)
                    if f"StartupWMClass={search_term}" in content:
                        info["score"] += 3
                    if f"Exec={search_term}" in content:
                        info["score"] += 2
                    if search_term.lower() == desktop_file.stem.lower():
                        info["score"] += 4
                        
                    all_matches.append(info)
                    
            except (UnicodeDecodeError, PermissionError):
                continue
                
    if not all_matches:
        return None
        
    # Sort by: main entries first, then by score, then by path length
    all_matches.sort(key=lambda x: (
        -x['is_main'], 
        -x['score'],
        len(x['path'])
        )
    )
    
    return all_matches[0]

def get_desktop_info(desktop_path):
    info = {"icon": ""}
    try:
        with open(desktop_path, 'r') as f:
            for line in f:
                if line.startswith("Icon="):
                    info["icon"] = line.split("=", 1)[1].strip()
    except (UnicodeDecodeError, PermissionError, FileNotFoundError):
        pass
    return info

def get_windows_class_names() -> None:
    class_names = {}
    for k, v in hyprland._windows.items():
        class_names[k] = v._class_name
    return class_names

def find_apps_data_best_match(class_names) -> None:
    best_matched_apps = {}
    best_match = None
    for win_id, class_name in class_names.items():
        app_data = find_app_data_best_match(class_name)
        if app_data is not None:
            best_matched_apps[win_id] = app_data
    return best_matched_apps

def find_app_data_best_match(class_name) -> None:
    best_match = None
    match = find_best_desktop_match(class_name)
    if match and (not best_match or match['score'] > best_match['score']):
        best_match = match
    if best_match and best_match['score'] >= 4:  # Found perfect match
        desktop_info = get_desktop_info(best_match['path'])
        print(desktop_info['icon'])
        return {
                'icon': desktop_info['icon']
                }
    return None

def create_app_button(app, win_id):
    return widgets.Button(
                child=widgets.Icon(image=app['icon'], pixel_size=32),
                css_classes=["tasklist-item", "unset"],
                on_click=lambda self: focus_window(win_id)
            )

def focus_window(win_id):
    subprocess.run(
        ["hyprctl", "dispatch", "focuswindow", "address:" + win_id]
    )

class TaskList(widgets.Box):
    running_apps = {}

    def __init__(self):
        super().__init__()
        hyprland.connect("window_added", lambda x, window: self.on_win_add(window))
        self.on_init()
    
    def on_init(self) -> None:
        winid_class_names = get_windows_class_names()
        self.running_apps = find_apps_data_best_match(winid_class_names)
        self.sync()
        for k, v in hyprland._windows.items():
            self.bind_win_close_event(v)

    def bind_win_close_event(self, window):
        window.connect('closed', lambda win: self.on_win_closed(win))
    
    def on_win_closed(self, win):
        self.running_apps.pop(win._address, None)
        self.sync()

    def on_win_add(self, window) -> None:
        new_app = find_app_data_best_match(window._class_name)
        if new_app is None:
            return

        self.bind_win_close_event(window)
        self.running_apps[window._address] = new_app
        self.sync()
    
    def sync(self):
        app_buttons = []
        for win_id, app in self.running_apps.items():
            app_buttons.append(create_app_button(app, win_id))

        self.child = app_buttons