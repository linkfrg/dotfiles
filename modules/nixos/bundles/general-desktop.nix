{
  config,
  lib,
  ...
}: let
  cfg = config.custom.bundles.general-desktop;
in {
  options.custom.bundles.general-desktop = {
    enable = lib.mkEnableOption "Enable General Desktop NixOS bundle";
  };

  config = lib.mkIf cfg.enable {
    custom = {
      core = {
        enable = true;
        bootloader.enable = true;
        locale.enable = true;
        networking = {
          enable = true;
        };
        users = {
          enable = true;
          username = "link";
        };
      };

      desktop = {
        hyprland.enable = true;
      };

      hardware = {
        firmware.enable = true;
        vxeMouse.enable = true;
        intelMicrocode.enable = true;
      };

      programs = {
        steam.enable = true;
        thunar.enable = true;
      };

      services = {
        avahi.enable = true;
        flatpak.enable = true;
        imobiledevice.enable = true;
        pipewire.enable = true;
        zram.enable = true;
        docker.enable = true;
        networkmanager.enable = true;
        gc.enable = true;
      };

      terminal = {
        common.enable = true;
        fish.enable = true;
        micro.enable = true;
      };
    };
  };
}
