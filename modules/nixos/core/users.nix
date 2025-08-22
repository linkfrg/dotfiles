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
