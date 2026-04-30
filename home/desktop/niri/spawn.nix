{
  spawn-at-startup = [
    {
        argv = ["dbus-update-activation-environment" "--systemd" "WAYLAND_DISPLAY" "XDG_CURRENT_DESKTOP"];
    }
    {
      argv = ["ignis" "init"];
    }
    {
      argv = ["AyuGram" "-startintray"];
    }
  ];
}
