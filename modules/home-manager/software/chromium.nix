{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.software.chromium;
in {
  options.linkfrg-dotfiles.software.chromium = {
    enable = lib.mkEnableOption "Enable chromium";
  };

  config = lib.mkIf cfg.enable {
    programs.chromium.enable = true;
  };
}
