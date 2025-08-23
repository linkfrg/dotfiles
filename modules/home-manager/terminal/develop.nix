{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.terminal.develop;
in {
  options.custom.terminal.develop = {
    enable = lib.mkEnableOption "Enable developer utils";
  };

  config = lib.mkIf cfg.enable {
    home.packages = with pkgs; [
      cloc
      act
    ];
  };
}
