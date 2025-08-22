{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.services.zram;
in {
  options.linkfrg-dotfiles.services.zram = {
    enable = lib.mkEnableOption "Enable zram";
  };

  config = lib.mkIf cfg.enable {
    zramSwap.enable = true;
  };
}
