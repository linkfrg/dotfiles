{
  pkgs,
  modulesPath,
  ...
}: {
  imports = [
    ../../system/core/nix.nix
    ../../system/services/imobiledevice.nix
    ../../system/services/networkmanager.nix
    ../../system/terminal.nix
    "${modulesPath}/installer/cd-dvd/installation-cd-minimal.nix"
  ];

  users.users.nixos.shell = pkgs.fish;

  nixpkgs.hostPlatform = "x86_64-linux";
}
