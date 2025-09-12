{
  inputs,
  outputs,
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

    terminal = {
      nvtop = {
        enable = true;
        intel = true;
      };
    };
  };

  wayland.windowManager.hyprland.settings = {
    monitor = [
      "eDP-1, 1920x1080@60, 0x0, 1.2"
    ];

    xwayland = {
      force_zero_scaling = true;
    };
  };
}
