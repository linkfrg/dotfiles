{lib, ...}: {
  imports = [
    ./hardware-configuration.nix
    ./disk-config.nix
    ../../system/core/nix.nix
    ../../system/core/grub.nix
    ../../system/core/locale.nix
    ../../system/core/users.nix
    ../../system/core/suspend-then-hibernate.nix
    ../../system/desktop/niri.nix
    ../../system/hardware/intel-graphics.nix
    ../../system/hardware/vxe-mouse.nix
    ../../system/hardware/bluetooth.nix
    ../../system/services/firewall.nix
    ../../system/services/flatpak.nix
    ../../system/services/gc.nix
    ../../system/services/networkmanager.nix
    ../../system/services/pipewire.nix
    ../../system/services/power-profiles.nix
    ../../system/services/upower.nix
    ../../system/services/navidrome.nix
    ../../system/services/ly.nix
    ../../system/software
    ../../system/terminal.nix
    ../../system/home-manager.nix
  ];

  networking.hostName = "laptop";

  services.logind.settings.Login.HandlePowerKey = "ignore";

  # One of the usb ports is dead and kernel stucks in a loop trying to power-manage it
  # leading to kworker loading CPU up to 10% overall and 100% on one core
  # So, this disables Power Management on usb3
  #
  # To debug use btop and
  # $ sudo -s
  # $ echo l > /proc/sysrq-trigger
  # $ dmesg -w
  services.udev.extraRules = ''
    ACTION=="add", SUBSYSTEM=="usb", KERNEL=="usb3", ATTR{power/control}="on"
  '';

  home-manager.users.link = {
    imports = [
      ../../home/services/hypridle
    ];
    programs.niri.settings.outputs = {
      "eDP-1" = {
        mode = {
          height = 1080;
          width = 1920;
          refresh = 60.0;
        };
        scale = 1.2;
        variable-refresh-rate = true;
      };
    };

    wayland.windowManager.hyprland.settings = {
      monitor = [
        "eDP-1, 1920x1080@60, 0x0, 1.2"
      ];

      xwayland = {
        force_zero_scaling = true;
      };

      input = {
        touchpad = {
          scroll_factor = 0.75;
        };
      };

      gesture = [
        "3, horizontal, workspace"
      ];
      # battery saving
      decoration.blur.enabled = lib.mkForce false;
      decoration.shadow.enabled = lib.mkForce false;

      misc = {
        vfr = true;
      };

      device = [
        {
          name = "elan0528:00-04f3:321b-touchpad";
          accel_profile = "adaptive";
          sensitivity = 0.15;
        }
      ];
    };
  };

  system.stateVersion = "25.05";
}
