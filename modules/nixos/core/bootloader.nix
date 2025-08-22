{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.core.bootloader;
in {
  options.linkfrg-dotfiles.core.bootloader = {
    enable = lib.mkEnableOption "Enable bootloader";
  };

  config = lib.mkIf cfg.enable {
    boot.loader = {
      systemd-boot.enable = true;
      efi.canTouchEfiVariables = true;
    };
  };
}
