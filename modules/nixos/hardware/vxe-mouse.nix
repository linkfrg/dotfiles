{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.hardware.vxeMouse;
in {
  options.linkfrg-dotfiles.hardware.vxeMouse = {
    enable = lib.mkEnableOption "Make ATK Hub work";
  };

  config = lib.mkIf cfg.enable {
    services.udev.extraRules = ''
      KERNEL=="hidraw*", ATTRS{idVendor}=="3554", MODE="0666"
    '';
  };
}
