{
  config,
  lib,
  ...
}: let
  cfg = config.custom.hardware.firmware;
in {
  options.custom.hardware.firmware = {
    enable = lib.mkEnableOption "Enable firmware";
  };

  config = lib.mkIf cfg.enable {
    hardware.enableRedistributableFirmware = true;
  };
}
