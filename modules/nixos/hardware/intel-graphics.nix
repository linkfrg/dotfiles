{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.hardware.intel-graphics;
in {
  options.custom.hardware.intel-graphics = {
    enable = lib.mkEnableOption "Enable Intel Graphics";
  };

  config = lib.mkIf cfg.enable {
    services.xserver.videoDrivers = ["modesetting"];

    hardware.graphics = {
      enable = true;
      extraPackages = with pkgs; [
        # For modern Intel CPU's
        intel-media-driver # Enable Hardware Acceleration
        vpl-gpu-rt # Enable QSV
      ];
    };
    environment.sessionVariables = {LIBVA_DRIVER_NAME = "iHD";};
  };
}
