{
  config,
  pkgs,
  lib,
  ...
}: let
  cfg = config.custom.terminal.common;
in {
  options.custom.terminal.common = {
    enable = lib.mkEnableOption "Enable common utils";
  };

  config = lib.mkIf cfg.enable {
    home.packages = with pkgs; [
      cmatrix
      cava
      gh
      speedtest-cli
      yazi
    ];
  };
}
