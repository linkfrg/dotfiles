{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.hardware.firmware;
in {
  options.linkfrg-dotfiles.hardware.firmware = {
    enable = lib.mkEnableOption "Enable firmware";
  };

  config = lib.mkIf cfg.enable {
    hardware.enableRedistributableFirmware = true;
  };
}
