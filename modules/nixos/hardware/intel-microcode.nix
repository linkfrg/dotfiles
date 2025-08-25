{
  config,
  lib,
  ...
}: let
  cfg = config.custom.hardware.intelMicrocode;
in {
  options.custom.hardware.intelMicrocode = {
    enable = lib.mkEnableOption "Enable Intel microcode updates";
  };

  config = lib.mkIf cfg.enable {
    hardware.cpu.intel.updateMicrocode = true;
  };
}
