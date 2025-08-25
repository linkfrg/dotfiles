{
  imports = [
    ./hardware-configuration.nix
    ../common/nixos.nix
  ];

  custom = {
    core = {
      networking = {
        hostName = "laptop";
      };
    };

    hardware = {
      dataDisk = {
        enable = true;
        uuid = "12beb1b5-0f4f-4b0c-8c86-988d3868d2b1";
        fsType = "xfs";
      };
    };

    services = {
      upower.enable = true;
    };
  };
}
