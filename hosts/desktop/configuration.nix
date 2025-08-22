{
  imports = [
    ./hardware-configuration.nix
    ../common/nixos.nix
  ];

  linkfrg-dotfiles = {
    core = {
      networking = {
        hostName = "desktop";
      };
    };

    hardware = {
      nvidia.enable = true;

      dataDisk = {
        enable = true;
        uuid = "878866d6-3892-4b13-a265-37b96aae8345";
        fsType = "ext4";
      };
    };

    programs = {
      virt-manager.enable = true;
    };
  };
}
