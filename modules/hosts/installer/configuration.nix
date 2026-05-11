{ self, inputs, ... }:
{

  flake.nixosConfigurations.installer = inputs.nixpkgs.lib.nixosSystem {
    modules = [ self.nixosModules.installerConfiguration ];
  };

  flake.nixosModules.installerConfiguration =
    {
      pkgs,
      modulesPath,
      ...
    }:
    {

      imports = [
        self.nixosModules.nix
        self.nixosModules.imobiledevice
        self.nixosModules.networkmanager
        self.nixosModules.terminalPrograms
        "${modulesPath}/installer/cd-dvd/installation-cd-minimal.nix"
      ];

      users.users.nixos.shell = pkgs.fish;

      nixpkgs.hostPlatform = "x86_64-linux";
    };
}
