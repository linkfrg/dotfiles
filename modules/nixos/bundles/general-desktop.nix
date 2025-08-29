{
  config,
  lib,
  pkgs,
  ...
}: let
  cfg = config.custom.bundles.general-desktop;
in {
  options.custom.bundles.general-desktop = {
    enable = lib.mkEnableOption "Enable General Desktop NixOS bundle";
    hostName = lib.mkOption {
      type = lib.types.str;
      description = "The hostname to use";
    };
    username = lib.mkOption {
      type = lib.types.str;
      description = "The name of the user";
    };
  };

  config = lib.mkIf cfg.enable {
    networking.hostName = cfg.hostName;

    time.timeZone = "Asia/Almaty";
    i18n.defaultLocale = "en_US.UTF-8";

    i18n.extraLocaleSettings = {
      LC_ADDRESS = "en_US.UTF-8";
      LC_IDENTIFICATION = "en_US.UTF-8";
      LC_MEASUREMENT = "en_US.UTF-8";
      LC_MONETARY = "en_US.UTF-8";
      LC_NAME = "en_US.UTF-8";
      LC_NUMERIC = "en_US.UTF-8";
      LC_PAPER = "en_US.UTF-8";
      LC_TELEPHONE = "en_US.UTF-8";
      LC_TIME = "en_US.UTF-8";
    };

    users.users.${cfg.username} = {
      isNormalUser = true;
      shell = pkgs.fish;
      extraGroups = [
        "wheel"
        "input"
        "libvirtd"
        "docker"
        "networkmanager"
      ];
    };

    system.stateVersion = "25.05";

    custom = {
      core = {
        nix.enable = true;
        systemd-boot.enable = true;
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
        firewall.enable = true;
      };

      terminal = {
        common.enable = true;
        fish.enable = true;
        micro.enable = true;
      };
    };
  };
}
