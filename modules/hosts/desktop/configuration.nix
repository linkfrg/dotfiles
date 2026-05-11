{self, ...}: {
  flake.nixosModules.desktopConfiguration = {
    imports = [
      self.nixosModules.nixSettings
      self.nixosModules.systemdBoot
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

      self.nixosModules.nvidia
      self.nixosModules.desktopHardware
    ];

    networking.hostName = "desktop";

    home-manager.users.link = {
      programs.niri.settings.outputs = {
        "DP-1" = {
          mode = {
            height = 1080;
            width = 1920;
            refresh = 144.0;
          };
          position = {
            x = 1920;
            y = 0;
          };
          scale = 1;
        };

        "HDMI-A-1" = {
          mode = {
            height = 1080;
            width = 1920;
            refresh = 75.0;
          };
          position = {
            x = 0;
            y = 0;
          };
          scale = 1;
        };
      };
    };

    system.stateVersion = "25.05";
  };
}
