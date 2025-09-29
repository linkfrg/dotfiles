{
  config,
  lib,
  pkgs,
  ...
}: let
  cfg = config.custom.games;
in {
  options.custom.games = {
    enable = lib.mkEnableOption "Enable Non-steam games";
  };

  config = lib.mkIf cfg.enable {
    home.packages = with pkgs; [
      prismlauncher
      osu-lazer-bin
    ];
  };
}
