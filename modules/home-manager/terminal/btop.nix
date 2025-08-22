{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.terminal.btop;
in {
  options.linkfrg-dotfiles.terminal.btop = {
    enable = lib.mkEnableOption "Enable btop";
  };

  config = lib.mkIf cfg.enable {
    programs.btop.enable = true;
  };
}
