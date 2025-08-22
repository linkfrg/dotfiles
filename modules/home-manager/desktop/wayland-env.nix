{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.desktop.waylandEnv;
in {
  options.linkfrg-dotfiles.desktop.waylandEnv = {
    enable = lib.mkEnableOption "Enable Wayland env vars";
  };

  config = lib.mkIf cfg.enable {
    home.sessionVariables = {
      # Electron
      NIXOS_OZONE_WL = "1";

      # Firefox
      EGL_PLATFORM = "wayland";
      MOZ_ENABLE_WAYLAND = "1";

      # For qt apps
      QT_QPA_PLATFORM = "wayland";
      QT_QPA_PLATFORMTHEME = "qt5ct";
    };
  };
}
