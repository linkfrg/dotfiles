{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.hardware.intelMicrocode;
in {
  options.linkfrg-dotfiles.hardware.intelMicrocode = {
    enable = lib.mkEnableOption "Enable Intel microcode updates";
  };

  config = lib.mkIf cfg.enable {
    hardware.cpu.intel.updateMicrocode = true;
  };
}
