{
  config,
  lib,
  ...
}: let
  cfg = config.custom.software.chromium;
in {
  options.custom.software.chromium = {
    enable = lib.mkEnableOption "Enable chromium";
  };

  config = lib.mkIf cfg.enable {
    programs.chromium.enable = true;
  };
}
