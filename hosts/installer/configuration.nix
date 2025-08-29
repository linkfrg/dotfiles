{
  pkgs,
  modulesPath,
  outputs,
  ...
}: {
  imports = [
    "${modulesPath}/installer/cd-dvd/installation-cd-minimal.nix"
    outputs.nixosModules.default
  ];

  custom = {
    core = {
      nix.enable = true;
    };

    services = {
      imobiledevice.enable = true;
      networkmanager.enable = true;
    };
    terminal = {
      fish.enable = true;
      micro.enable = true;
    };
  };

  users.users.nixos.shell = pkgs.fish;

  nixpkgs.hostPlatform = "x86_64-linux";
}
