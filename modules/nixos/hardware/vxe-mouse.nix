{
  config,
  lib,
  ...
}: let
  cfg = config.custom.hardware.vxeMouse;
in {
  options.custom.hardware.vxeMouse = {
    enable = lib.mkEnableOption "Make ATK Hub work";
  };

  config = lib.mkIf cfg.enable {
    services.udev.extraRules = ''
      KERNEL=="hidraw*", ATTRS{idVendor}=="3554", MODE="0666"
    '';
  };
}
