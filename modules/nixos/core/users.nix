{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.core.users;
in {
  options.linkfrg-dotfiles.core.users = {
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
        "networkmanager"
        "wheel"
        "input"
      ];
    };
  };
}
