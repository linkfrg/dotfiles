{
  config,
  lib,
  ...
}: let
  cfg = config.custom.services.gc;
in {
  options.custom.services.gc = {
    enable = lib.mkEnableOption "Enable Nix garbage collection";
  };

  config = lib.mkIf cfg.enable {
    boot.loader.systemd-boot.configurationLimit = 5;

    nix.gc = {
      automatic = true;
      dates = "weekly";
      options = "--delete-older-than 1w";
    };

    nix.settings.auto-optimise-store = true;
  };
}
