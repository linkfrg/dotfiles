{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.services.imobiledevice;
in {
  options.linkfrg-dotfiles.services.imobiledevice = {
    enable = lib.mkEnableOption "Enable imobiledevice and usbmuxd";
  };

  config = lib.mkIf cfg.enable {
    environment.systemPackages = with pkgs; [
      libimobiledevice
    ];

    services.usbmuxd.enable = true;
  };
}
