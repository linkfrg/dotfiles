{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.terminal.direnv;
in {
  options.linkfrg-dotfiles.terminal.direnv = {
    enable = lib.mkEnableOption "Enable direnv";
  };

  config = lib.mkIf cfg.enable {
    programs.direnv = {
      enable = true;
      # enableFishIntegration = true;
      nix-direnv.enable = true;
      silent = true;
    };
  };
}
