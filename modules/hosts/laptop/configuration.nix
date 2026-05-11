{
  self,
  inputs,
  ...
}: {
  flake.nixosConfigurations.laptop = inputs.nixpkgs.lib.nixosSystem {
    modules = [self.nixosModules.laptopConfiguration];
  };

  flake.nixosModules.laptopConfiguration = {
    pkgs,
    lib,
    ...
  }: {
    imports = [
      self.nixosModules.nixSettings
      self.nixosModules.grub
      self.nixosModules.latestKernel
      self.nixosModules.localeSettings
      self.nixosModules.linkUser
      self.nixosModules.dnsSettings

      self.nixosModules.niri

      self.nixosModules.vxeMouse
      self.nixosModules.docker
      self.nixosModules.flatpak
      self.nixosModules.gc
      self.nixosModules.networkManager
      self.nixosModules.pipewire
      self.nixosModules.powerProfilesDaemon
      self.nixosModules.cloudflareWarp
      self.nixosModules.nixLd
      self.nixosModules.keyd
      self.nixosModules.sops

      self.nixosModules.steam
      self.nixosModules.terminalPrograms

      self.nixosModules.homeManager
      self.nixosModules.laptopHardware
      self.nixosModules.laptopDisk

      self.nixosModules.suspendThenHibernate

      self.nixosModules.intelGraphics
      self.nixosModules.bluetooth
      self.nixosModules.powerProfilesDaemon
      self.nixosModules.upower
    ];

    networking.hostName = "laptop";
    services.logind.settings.Login.HandlePowerKey = "ignore";
    home-manager.users.link = {
      imports = [
        self.homeModules.hypridle
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

      programs.niri.settings.spawn-at-startup = [
        {
          argv = ["obsidian"];
        }
        {
          argv = ["ferdium"];
        }
        {
          argv = ["super-productivity"];
        }
      ];

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

    systemd.tmpfiles.rules = [
      "d /sdcard 777 root root -"
    ];

    fileSystems."/sdcard" = {
      device = "/dev/disk/by-uuid/c72ba4c3-48c3-497f-8fdd-3cc2eac6f6aa";
      fsType = "btrfs";
      options = [
        "noatime"
        "compress=zstd"
        "ssd"
        "discard=async"
      ];
    };

    system.stateVersion = "25.05";
  };
}
