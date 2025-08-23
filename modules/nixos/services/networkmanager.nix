{
  lib,
  config,
  ...
}: let
  cfg = config.linkfrg-dotfiles.services.networkmanager;
in {
  options.linkfrg-dotfiles.services.networkmanager = {
    enable = lib.mkEnableOption "Enable Network Manager";
  };

  config = lib.mkIf cfg.enable {
    networking.networkmanager.enable = true;
    systemd.services.NetworkManager-wait-online.enable = false;
    users.users.${config.linkfrg-dotfiles.core.users.username}.extraGroups = ["networkmanager"];
  };
}
