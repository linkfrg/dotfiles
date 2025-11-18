{inputs, ...}: {
  imports = [
    ../../home/main.nix
    ../../home/games.nix
    ../../home/terminal
    ../../home/software
    ../../home/software/firefox-nvidia.nix
    ../../home/services
    ../../home/desktop/niri
    ../../home/desktop/hyprlock
    ../../home/desktop/ignis.nix
    ../../home/desktop/fonts.nix
    ../../home/desktop/pointer-cursor.nix
    inputs.dotfiles-private.homeManagerModules.default
  ];

  wayland.windowManager.hyprland.settings = {
    monitor = [
      "DP-1, 1920x1080@144, 1920x0, 1"
      "HDMI-A-1, 1920x1080@75, 0x0, 1"
    ];

    workspace = [
      "1, monitor:DP-1, default:true"
      "2, monitor:DP-1"
      "3, monitor:DP-1"
      "4, monitor:DP-1"
      "5, monitor:DP-1"
      "6, monitor:DP-1"
      "7, monitor:DP-1"
      "8, monitor:DP-1"
      "9, monitor:DP-1"
      "10, monitor:HDMI-A-1"
    ];
  };
}
