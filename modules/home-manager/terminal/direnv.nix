{
  config,
  lib,
  ...
}: let
  cfg = config.custom.terminal.direnv;
in {
  options.custom.terminal.direnv = {
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
