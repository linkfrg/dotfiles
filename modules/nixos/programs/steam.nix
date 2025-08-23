{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.programs.steam;
in {
  options.custom.programs.steam = {
    enable = lib.mkEnableOption "Enable Steam and all other gaming stuff";
  };

  config = lib.mkIf cfg.enable {
    programs.steam = {
      enable = true;
      gamescopeSession.enable = true;
      extraCompatPackages = [pkgs.proton-ge-bin];
    };

    programs.gamemode.enable = true;
  };
}
