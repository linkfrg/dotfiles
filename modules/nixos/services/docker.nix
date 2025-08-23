{
  config,
  lib,
  ...
}: let
  cfg = config.custom.services.docker;
in {
  options.custom.services.docker = {
    enable = lib.mkEnableOption "Enable docker";
  };

  config = lib.mkIf cfg.enable {
    virtualisation.docker.enable = true;
    users.users.${config.custom.core.users.username}.extraGroups = ["docker"];
  };
}
