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
        uuid = "f086eeb3-5866-48ab-a320-daf9ee96fe03";
        fsType = "btrfs";
        fsOptions = ["compress=zstd:3"];
      };
    };

    services = {
      upower.enable = true;
      power-profiles.enable = true;
      zram.enable = lib.mkForce false;
    };
  };
}
