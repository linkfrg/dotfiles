{
  lib,
  config,
  ...
}: let
  cfg = config.custom.core.grub;
in {
  options.custom.core.grub = {
    enable = lib.mkEnableOption "Enable GRUB bootloader";
  };

  config = lib.mkIf cfg.enable {
    boot.loader = {
      efi.canTouchEfiVariables = true;
      grub = {
        enable = true;
        efiSupport = true;
        useOSProber = true;
        device = "nodev";
      };
    };
  };
}
