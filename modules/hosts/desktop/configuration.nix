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
      self.nixosModules.imobiledevice
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

      self.nixosModules.nvidia
      self.nixosModules.desktopHardware
    ];

    networking.hostName = "desktop";

    home-manager.users.link = {
      xdg.configFile."niri/device-specific.kdl".source = ../../../config/niri/desktop.kdl;
    };

    system.stateVersion = "25.05";
  };
}
