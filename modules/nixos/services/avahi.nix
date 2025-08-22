{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.services.avahi;
in {
  options.linkfrg-dotfiles.services.avahi = {
    enable = lib.mkEnableOption "Enable Avahi";
  };

  config = lib.mkIf cfg.enable {
    services.avahi = {
      enable = true;
      nssmdns4 = true;

      publish = {
        enable = true;
        userServices = true;
        addresses = true;
      };
    };
  };
}
