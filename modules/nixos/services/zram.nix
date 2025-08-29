{
  config,
  lib,
  ...
}: let
  cfg = config.custom.services.zram;
in {
  options.custom.services.zram = {
    enable = lib.mkEnableOption "Enable zram";
  };

  config = lib.mkIf cfg.enable {
    zramSwap.enable = true;
  };
}
