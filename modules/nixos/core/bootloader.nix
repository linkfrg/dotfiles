{
  config,
  lib,
  ...
}: let
  cfg = config.custom.core.bootloader;
in {
  options.custom.core.bootloader = {
    enable = lib.mkEnableOption "Enable bootloader";
  };

  config = lib.mkIf cfg.enable {
    boot.loader = {
      systemd-boot.enable = true;
      efi.canTouchEfiVariables = true;
    };
  };
}
