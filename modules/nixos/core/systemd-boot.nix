{
  config,
  lib,
  ...
}: let
  cfg = config.custom.core.systemd-boot;
in {
  options.custom.core.systemd-boot = {
    enable = lib.mkEnableOption "Enable systemd-boot";
  };

  config = lib.mkIf cfg.enable {
    boot.loader = {
      systemd-boot.enable = true;
      efi.canTouchEfiVariables = true;
    };
  };
}
