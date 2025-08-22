{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.services.gitea;
in {
  options.linkfrg-dotfiles.services.gitea = {
    enable = lib.mkEnableOption "Enable gitea on localhost";
  };

  config = lib.mkIf cfg.enable {
    services.gitea = {
      enable = true;
      user = "gitea";
      database = {
        type = "sqlite3";
      };
      httpPort = 3000;
      rootUrl = "http://localhost:3000/";
    };
  };
}
