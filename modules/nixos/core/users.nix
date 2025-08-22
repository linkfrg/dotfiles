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
  };

  config = lib.mkIf cfg.enable {
    users.users.link = {
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
