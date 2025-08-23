{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.services.imobiledevice;
in {
  options.custom.services.imobiledevice = {
    enable = lib.mkEnableOption "Enable imobiledevice and usbmuxd";
  };

  config = lib.mkIf cfg.enable {
    environment.systemPackages = with pkgs; [
      libimobiledevice
    ];

    services.usbmuxd.enable = true;
  };
}
