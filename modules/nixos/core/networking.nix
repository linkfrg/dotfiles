{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.core.networking;
in {
  options.linkfrg-dotfiles.core.networking = {
    enable = lib.mkEnableOption "Enable networking settings";
    hostName = lib.mkOption {
      type = lib.types.str;
      description = "The hostname to use";
    };
  };

  config = lib.mkIf cfg.enable {
    networking.hostName = cfg.hostName;

    networking.firewall = {
      # make wireguard work
      checkReversePath = false;

      # make UxPlay work (launch with ``uxplay -p``)
      allowedUDPPorts = [7011 6001 6000];
      allowedTCPPorts = [7100 7000 7001];
    };
  };
}
