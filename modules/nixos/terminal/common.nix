{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.terminal.common;
in {
  options.linkfrg-dotfiles.terminal.common = {
    enable = lib.mkEnableOption "Enable common utils";
  };

  config = lib.mkIf cfg.enable {
    environment.systemPackages = with pkgs; [
      usbutils
      libva-utils
      tree
      file
    ];
  };
}
