{
  config,
  lib,
  ...
}: let
  cfg = config.custom.services.firewall;
in {
  options.custom.services.firewall = {
    enable = lib.mkEnableOption "Enable firewall settings";
  };

  config = lib.mkIf cfg.enable {
    networking.firewall = {
      enable = false;
      # make wireguard work
      checkReversePath = false;

      # make UxPlay work (launch with ``uxplay -p``)
      allowedUDPPorts = [7011 6001 6000];
      allowedTCPPorts = [7100 7000 7001];
    };
  };
}
