{
  config,
  lib,
  ...
}: let
  cfg = config.custom.services.pipewire;
in {
  options.custom.services.pipewire = {
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
