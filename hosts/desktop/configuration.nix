{inputs, ...}: {
  imports = [
    ./hardware-configuration.nix
    ../../system/core/nix.nix
    ../../system/core/grub.nix
    ../../system/core/locale.nix
    ../../system/core/users.nix
    ../../system/desktop/niri.nix
    ../../system/hardware/intel-graphics.nix
    ../../system/hardware/vxe-mouse.nix
    ../../system/services/firewall.nix
    ../../system/services/flatpak.nix
    ../../system/services/gc.nix
    ../../system/services/networkmanager.nix
    ../../system/services/pipewire.nix
    ../../system/services/power-profiles.nix
    ../../system/services/upower.nix
    ../../system/software
    ../../system/terminal.nix
    inputs.dotfiles-private.nixosModules.default
  ];

  networking.hostName = "desktop";
  system.stateVersion = "25.05";
}
