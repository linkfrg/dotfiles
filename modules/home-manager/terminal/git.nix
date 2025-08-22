{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.terminal.git;
in {
  options.linkfrg-dotfiles.terminal.git = {
    enable = lib.mkEnableOption "Enable git";
  };

  config = lib.mkIf cfg.enable {
    programs.git = {
      enable = true;
      userName = "Link";
      userEmail = "linkfrg.dev@proton.me";

      extraConfig = {
        init.defaultBranch = "main";
      };
    };
  };
}
