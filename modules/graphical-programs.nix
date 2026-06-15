{
  flake.nixosModules.thunar = {pkgs, ...}: {
    programs.thunar = {
      enable = true;
      plugins = with pkgs; [
        thunar-archive-plugin
      ];
    };

    environment.systemPackages = with pkgs; [
      file-roller
    ];

    services.gvfs.enable = true;
    services.tumbler.enable = true;
  };
  flake.nixosModules.virt-manager = {pkgs, ...}: {
    virtualisation.libvirtd = {
      enable = true;
      qemu.vhostUserPackages = with pkgs; [virtiofsd];
    };
    programs.virt-manager.enable = true;
    virtualisation.spiceUSBRedirection.enable = true;

    environment.systemPackages = with pkgs; [
      dnsmasq
    ];

    networking.firewall.trustedInterfaces = ["virbr0"];
  };

  flake.homeModules.graphicalPrograms = {pkgs, ...}: {
    programs.mpv = {
      enable = true;
      config = {
        audio-file-auto = "fuzzy";
      };
    };

    home.packages = with pkgs; [
      telegram-desktop
      ayugram-desktop
      vesktop
      proton-vpn
      eog
      transmission_4-gtk
      xeyes
      gnome-calculator
      snapshot
      pavucontrol
      obsidian
      ferdium
      gapless
      super-productivity
      libreoffice
    ];
  };
}
