{
  imports = [
    ./hardware-configuration.nix
    ../../system/core/nix.nix
    ../../system/core/systemd-boot.nix
    ../../system/core/locale.nix
    ../../system/core/users.nix
    ../../system/desktop/niri.nix
    ../../system/hardware/nvidia.nix
    ../../system/hardware/vxe-mouse.nix
    ../../system/hardware/bluetooth.nix
    ../../system/services/firewall.nix
    ../../system/services/flatpak.nix
    ../../system/services/gc.nix
    ../../system/services/networkmanager.nix
    ../../system/services/pipewire.nix
    ../../system/services/imobiledevice.nix
    ../../system/services/navidrome.nix
    ../../system/services/distrobox.nix
    ../../system/services/cloudflare-warp.nix
    ../../system/services/nix-ld.nix
    ../../system/desktop/gdm.nix
    ../../system/software
    ../../system/terminal.nix
    ../../system/home-manager.nix
  ];

  networking.hostName = "desktop";

  home-manager.users.link = {
    programs.niri.settings.outputs = {
      "DP-1" = {
        mode = {
          height = 1080;
          width = 1920;
          refresh = 144.0;
        };
        position = {
          x = 1920;
          y = 0;
        };
        scale = 1;
      };

      "HDMI-A-1" = {
        mode = {
          height = 1080;
          width = 1920;
          refresh = 75.0;
        };
        position = {
          x = 0;
          y = 0;
        };
        scale = 1;
      };
    };

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
