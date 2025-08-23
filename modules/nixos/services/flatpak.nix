{
  config,
  lib,
  ...
}: let
  cfg = config.custom.services.flatpak;
in {
  options.custom.services.flatpak = {
    enable = lib.mkEnableOption "Enable flatpak";
  };

  config = lib.mkIf cfg.enable {
    services.flatpak.enable = true;
  };
}
