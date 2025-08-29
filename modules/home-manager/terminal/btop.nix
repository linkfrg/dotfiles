{
  config,
  lib,
  ...
}: let
  cfg = config.custom.terminal.btop;
in {
  options.custom.terminal.btop = {
    enable = lib.mkEnableOption "Enable btop";
  };

  config = lib.mkIf cfg.enable {
    programs.btop.enable = true;
  };
}
