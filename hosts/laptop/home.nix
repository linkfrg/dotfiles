{
  inputs,
  outputs,
  lib,
  ...
}: {
  imports = [
    outputs.homeManagerModules.default
    outputs.homeManagerModules.public
    inputs.dotfiles-private.homeManagerModules.default
  ];

  custom = {
    bundles.general-desktop = {
      enable = true;
      username = "link";
    };

    desktop.niri.enable = true;

    terminal = {
      nvtop = {
        enable = true;
        intel = true;
      };
    };

    services = {
      hypridle.enable = true;
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
