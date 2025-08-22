{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.core.gc;
in {
  options.linkfrg-dotfiles.core.gc = {
    enable = lib.mkEnableOption "Enable garbage collection";
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
