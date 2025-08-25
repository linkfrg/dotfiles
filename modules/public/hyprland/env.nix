{
  env = [
    # Electron
    "NIXOS_OZONE_WL, 1"

    # Firefox
    "EGL_PLATFORM, wayland"
    "MOZ_ENABLE_WAYLAND, 1"

    # For qt apps
    "QT_QPA_PLATFORM, wayland"
    "QT_QPA_PLATFORMTHEME, qt5ct"
  ];
}
