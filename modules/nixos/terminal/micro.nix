{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.terminal.micro;
in {
  options.linkfrg-dotfiles.terminal.micro = {
    enable = lib.mkEnableOption "Enable micro";
  };

  config = lib.mkIf cfg.enable {
    environment.systemPackages = with pkgs; [
      micro
    ];

    environment.variables.EDITOR = "micro";
  };
}
