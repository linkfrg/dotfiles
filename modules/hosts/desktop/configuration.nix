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
      self.nixosModules.virt-manager

      self.nixosModules.homeManager

      self.nixosModules.nvidia
      self.nixosModules.bluetooth
      self.nixosModules.udisks
      self.nixosModules.desktopHardware
    ];

    networking.hostName = "desktop";

    home-manager.users.link = {
      xdg.configFile."niri/device-specific.kdl".source = ../../../config/niri/desktop.kdl;
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
        "nofail"
      ];
    };

    system.stateVersion = "25.05";
  };
}
