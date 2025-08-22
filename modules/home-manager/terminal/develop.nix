{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.terminal.develop;
in {
  options.linkfrg-dotfiles.terminal.develop = {
    enable = lib.mkEnableOption "Enable developer utils";
  };

  config = lib.mkIf cfg.enable {
    home.packages = with pkgs; [
      cloc
      act
    ];
  };
}
