{
  exec-once = [
    "ignis init"
    "/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1"
    "dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP"
  ];
}
