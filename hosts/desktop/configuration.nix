{
  imports = [
    ./hardware-configuration.nix
    ../../system/core/nix.nix
    ../../system/core/grub.nix
    ../../system/core/locale.nix
    ../../system/core/users.nix
    ../../system/desktop/niri.nix
    ../../system/hardware/intel-graphics.nix
    ../../system/hardware/vxe-mouse.nix
    ../../system/services/firewall.nix
    ../../system/services/flatpak.nix
    ../../system/services/gc.nix
    ../../system/services/networkmanager.nix
    ../../system/services/pipewire.nix
    ../../system/services/power-profiles.nix
    ../../system/services/upower.nix
    ../../system/software
    ../../system/terminal.nix
  ];

  networking.hostName = "desktop";

  home-manager.users.link = {
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
  };

  system.stateVersion = "25.05";
}
