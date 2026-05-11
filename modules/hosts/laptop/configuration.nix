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

      xdg.configFile."niri/device-specific.kdl".source = ../../../config/niri/laptop.kdl;
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
