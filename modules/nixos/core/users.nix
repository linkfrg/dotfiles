{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.core.users;
in {
  options.custom.core.users = {
    enable = lib.mkEnableOption "Enable users";
    username = lib.mkOption {
      type = lib.types.str;
      description = "The name of the user";
    };
  };

  config = lib.mkIf cfg.enable {
    users.users.${cfg.username} = {
      isNormalUser = true;
      shell = pkgs.fish;
      extraGroups = [
        "wheel"
        "input"
      ];
    };
  };
}
