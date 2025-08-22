{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.services.flatpak;
in {
  options.linkfrg-dotfiles.services.flatpak = {
    enable = lib.mkEnableOption "Enable flatpak";
  };

  config = lib.mkIf cfg.enable {
    services.flatpak.enable = true;
  };
}
