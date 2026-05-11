{
  flake.nixosModules.grub = {...}: {
    boot.loader = {
      efi.canTouchEfiVariables = true;
      grub = {
        enable = true;
        efiSupport = true;
        useOSProber = true;
        device = "nodev";
      };
    };
  };

  flake.nixosModules.systemdBoot = {...}: {
    boot.loader = {
      systemd-boot.enable = true;
      efi.canTouchEfiVariables = true;
    };
  };

  flake.nixosModules.localeSettings = {...}: {
    time.timeZone = "Asia/Almaty";
    i18n.defaultLocale = "en_US.UTF-8";

    i18n.extraLocaleSettings = {
      LC_ADDRESS = "en_US.UTF-8";
      LC_IDENTIFICATION = "en_US.UTF-8";
      LC_MEASUREMENT = "en_US.UTF-8";
      LC_MONETARY = "en_US.UTF-8";
      LC_NAME = "en_US.UTF-8";
      LC_NUMERIC = "en_US.UTF-8";
      LC_PAPER = "en_US.UTF-8";
      LC_TELEPHONE = "en_US.UTF-8";
      LC_TIME = "en_US.UTF-8";
    };
  };

  flake.nixosModules.nixSettings = {...}: {
    nixpkgs.config.allowUnfree = true;

    nix = {
      settings = {
        experimental-features = "nix-command flakes";
        flake-registry = "";
        nix-path = "";
      };
      channel.enable = false;
    };
  };

  flake.nixosModules.latestKernel = {pkgs, ...}: {
    boot.kernelPackages = pkgs.linuxPackages_latest;
  };
  flake.nixosModules.dnsSettings = {...}: {
    environment.etc."resolv.conf".text = ''
      nameserver 1.1.1.1
      nameserver 8.8.8.8
    '';
  };

  flake.nixosModules.gc = {
    boot.loader.systemd-boot.configurationLimit = 5;

    nix.gc = {
      automatic = true;
      dates = "weekly";
      options = "--delete-older-than 1w";
    };

    nix.settings.auto-optimise-store = true;
  };
}
