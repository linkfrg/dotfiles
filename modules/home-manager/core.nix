{
  config,
  lib,
  ...
}: let
  cfg = config.custom.core;
in {
  options.custom.core = {
    enable = lib.mkEnableOption "Enable core settings";
    username = lib.mkOption {
      type = lib.types.str;
      description = "The username";
    };
  };

  config = lib.mkIf cfg.enable {
    home = {
      username = cfg.username;
      homeDirectory = "/home/${cfg.username}";
    };

    nixpkgs = {
      config = {
        allowUnfree = true;
      };
    };

    programs.home-manager.enable = true;
    home.stateVersion = "25.05";
  };
}
