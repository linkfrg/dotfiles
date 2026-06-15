{
  flake.nixosModules.pipewire = {
    services.pipewire = {
      enable = true;
      alsa.enable = true;
      alsa.support32Bit = true;
      pulse.enable = true;
    };

    security.rtkit.enable = true;
  };

  flake.nixosModules.powerProfilesDaemon = {
    services.power-profiles-daemon.enable = true;
  };

  flake.nixosModules.zram = {
    zramSwap.enable = true;
  };

  flake.nixosModules.upower = {
    services.upower.enable = true;
  };

  flake.nixosModules.networkManager = {
    networking.networkmanager.enable = true;
    systemd.services.NetworkManager-wait-online.enable = false;
  };

  flake.nixosModules.docker = {
    virtualisation.docker.enable = true;
  };

  flake.nixosModules.flatpak = {
    services.flatpak.enable = true;
  };

  flake.nixosModules.imobiledevice = {pkgs, ...}: {
    environment.systemPackages = with pkgs; [
      libimobiledevice
    ];

    services.usbmuxd.enable = true;
  };

  flake.nixosModules.avahi = {
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

  flake.nixosModules.udisks = {
    services.udisks2.enable = true;
  };

  flake.nixosModules.cloudflareWarp = {
    services.cloudflare-warp = {
      enable = true;
    };
  };

  flake.nixosModules.keyd = {
    services.keyd = {
      enable = true;
      keyboards = {
        default = {
          ids = ["*"];
          settings = {
            main = {
              capslock = "overload(control, esc)";
            };
          };
        };
      };
    };
  };

  flake.nixosModules.suspendThenHibernate = {
    services.logind.settings.Login = {
      HandleLidSwitch = "suspend-then-hibernate";
      HandleLidSwitchExternalPower = "suspend-then-hibernate";
    };

    systemd.sleep.settings.Sleep = {
      HibernateDelaySec = "1h";
    };
  };

  flake.homeModules.wlsunset = {
    services.wlsunset = {
      enable = true;
      temperature = {
        day = 6500;
        night = 3000;
      };

      latitude = 52.5;
      longitude = 70.1;
    };
  };
}
