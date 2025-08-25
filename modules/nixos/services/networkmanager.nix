{
  lib,
  config,
  ...
}: let
  cfg = config.custom.services.networkmanager;
in {
  options.custom.services.networkmanager = {
    enable = lib.mkEnableOption "Enable Network Manager";
  };

  config = lib.mkIf cfg.enable {
    networking.networkmanager.enable = true;
    systemd.services.NetworkManager-wait-online.enable = false;
    users.users.${config.custom.core.users.username}.extraGroups = ["networkmanager"];
  };
}
