{
  inputs,
  lib,
  ...
}: {
  imports = [
    ../../home/main.nix
    ../../home/games.nix
    ../../home/terminal
    ../../home/software
    ../../home/services
    ../../home/desktop/niri
    ../../home/desktop/hyprlock
    ../../home/desktop/ignis.nix
    ../../home/desktop/fonts.nix
    ../../home/desktop/pointer-cursor.nix
    inputs.dotfiles-private.homeManagerModules.default
  ];

  programs.niri.settings.outputs = {
    "eDP-1" = {
      mode = {
        height = 1080;
        width = 1920;
        refresh = 60.0;
      };
      scale = 1.2;
      variable-refresh-rate = true;
    };
  };

  wayland.windowManager.hyprland.settings = {
    monitor = [
      "eDP-1, 1920x1080@60, 0x0, 1.2"
    ];

    xwayland = {
      force_zero_scaling = true;
    };

    input = {
      touchpad = {
        scroll_factor = 0.75;
      };
    };

    gesture = [
      "3, horizontal, workspace"
    ];
    # battery saving
    decoration.blur.enabled = lib.mkForce false;
    decoration.shadow.enabled = lib.mkForce false;

    misc = {
      vfr = true;
    };

    device = [
      {
        name = "elan0528:00-04f3:321b-touchpad";
        accel_profile = "adaptive";
        sensitivity = 0.15;
      }
    ];
  };
}
