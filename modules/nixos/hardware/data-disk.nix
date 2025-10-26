{
  config,
  lib,
  ...
}: let
  cfg = config.custom.hardware.dataDisk;
in {
  options.custom.hardware.dataDisk = {
    enable = lib.mkEnableOption "Automatically mount a disk to /data";

    uuid = lib.mkOption {
      type = lib.types.str;
      description = "The UUID of the disk";
    };

    fsType = lib.mkOption {
      type = lib.types.str;
      description = "The filesystem type";
    };

    fsOptions = lib.mkOption {
      type = with lib.types; listOf str;
      description = "Filesystem mount options";
      default = ["defaults"];
    };
  };

  config = lib.mkIf cfg.enable {
    systemd.tmpfiles.rules = [
      "d /data 777 root root -"
    ];

    fileSystems."/data" = {
      device = "/dev/disk/by-uuid/${cfg.uuid}";
      fsType = cfg.fsType;
      options = cfg.fsOptions;
    };
  };
}
