{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.services.pipewire;
in {
  options.linkfrg-dotfiles.services.pipewire = {
    enable = lib.mkEnableOption "Enable Pipewire";
  };

  config = lib.mkIf cfg.enable {
    services.pipewire = {
      enable = true;
      alsa.enable = true;
      alsa.support32Bit = true;
      pulse.enable = true;
    };

    security.rtkit.enable = true;
  };
}
