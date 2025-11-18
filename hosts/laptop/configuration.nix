{inputs, ...}: {
  imports = [
    ./hardware-configuration.nix
    ./disk-config.nix
    ../../system/core/nix.nix
    ../../system/core/grub.nix
    ../../system/core/locale.nix
    ../../system/core/users.nix
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
    ../../system/software
    ../../system/terminal.nix

    inputs.disko.nixosModules.disko
    inputs.dotfiles-private.nixosModules.default
  ];

  networking.hostName = "laptop";

  services.logind.settings.Login.HandlePowerKey = "ignore";
  services.gnome.gnome-keyring.enable = true;
  services.displayManager.gdm.enable = true;

  system.stateVersion = "25.05";
}
