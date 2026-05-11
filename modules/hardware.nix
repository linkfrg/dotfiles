{
  flake.nixosModules.bluetooth = {
    hardware.bluetooth.enable = true;
    services.blueman.enable = true;

    hardware.bluetooth.settings = {
      General = {
        ReconnectAttempts = 0;
      };
    };
  };

  flake.nixosModules.intelGraphics = {pkgs, ...}: {
    services.xserver.videoDrivers = ["modesetting"];

    hardware.graphics = {
      enable = true;
      extraPackages = with pkgs; [
        # For modern Intel CPU's
        intel-media-driver # Enable Hardware Acceleration
        vpl-gpu-rt # Enable QSV
        intel-compute-runtime
      ];
    };
    environment.sessionVariables = {
      LIBVA_DRIVER_NAME = "iHD";
    };
    hardware.enableRedistributableFirmware = true;
    boot.kernelParams = ["i915.enable_guc=3"];
  };

  flake.nixosModules.nvidia = {
    pkgs,
    config,
    ...
  }: {
    services.xserver.videoDrivers = ["nvidia"];

    environment.systemPackages = with pkgs; [
      vulkan-loader
      vulkan-validation-layers
      vulkan-tools
    ];

    hardware.nvidia = {
      modesetting.enable = true;
      powerManagement.enable = true;
      powerManagement.finegrained = false;
      open = true;
      nvidiaSettings = true;
      package = config.boot.kernelPackages.nvidiaPackages.stable;
    };

    environment.variables = {
      LIBVA_DRIVER_NAME = "nvidia";
      XDG_SESSION_TYPE = "wayland";
      GBM_BACKEND = "nvidia-drm";
      __GLX_VENDOR_LIBRARY_NAME = "nvidia";
      NVD_BACKEND = "direct";
    };
  };

  flake.nixosModules.vxeMouse = {
    services.udev.extraRules = ''
      KERNEL=="hidraw*", ATTRS{idVendor}=="3554", MODE="0666"
    '';
  };
}
