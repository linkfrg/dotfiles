{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.services.docker;
in {
  options.linkfrg-dotfiles.services.docker = {
    enable = lib.mkEnableOption "Enable docker";
  };

  config = lib.mkIf cfg.enable {
    virtualisation.docker.enable = true;
    users.users.link.extraGroups = ["docker"];
  };
}
