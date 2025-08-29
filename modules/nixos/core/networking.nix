{
  config,
  lib,
  ...
}: let
  cfg = config.custom.core.networking;
in {
  options.custom.core.networking = {
    enable = lib.mkEnableOption "Enable networking settings";
    hostName = lib.mkOption {
      type = lib.types.str;
      description = "The hostname to use";
    };
  };

  config = lib.mkIf cfg.enable {
    networking.hostName = cfg.hostName;
  };
}
