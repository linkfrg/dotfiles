{
  inputs,
  outputs,
  lib,
  ...
}: {
  imports = [
    ./hardware-configuration.nix
    outputs.nixosModules.default
    inputs.dotfiles-private.nixosModules.default
  ];

  custom = {
    bundles.general-desktop = {
      enable = true;
      hostName = "laptop";
      username = "link";
    };

    core = {
      systemd-boot.enable = lib.mkForce false;
      grub = {
        enable = true;
      };
    };

    hardware = {
      dataDisk = {
        enable = true;
        uuid = "41a66293-775b-41ea-8ea0-06a976587cae";
        fsType = "f2fs";
        fsOptions = ["defaults" "noatime" "compress_algorithm=zstd" "discard"];
      };
      intel-graphics.enable = true;
    };

    services = {
      upower.enable = true;
      power-profiles.enable = true;
      zram.enable = lib.mkForce false;
      docker.enable = lib.mkForce false;
    };
  };
  hardware.bluetooth.enable = true;
  services.blueman.enable = true;
}
