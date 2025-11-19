{
  description = "linkfrg's nix config";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

    home-manager = {
      url = "github:nix-community/home-manager";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    disko = {
      url = "github:nix-community/disko";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    ignis = {
      url = "github:ignis-sh/ignis";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    ignisctl-rs = {
      url = "github:linkfrg/ignisctl-rs";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    niri-flake = {
      url = "github:sodiboo/niri-flake";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    firefox-addons = {
      url = "gitlab:rycee/nur-expressions?dir=pkgs/firefox-addons";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    dotfiles-private = {
      url = "git+ssh://git@github.com/linkfrg/dotfiles-private.git";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {
    self,
    nixpkgs,
    home-manager,
    disko,
    dotfiles-private,
    niri-flake,
    ...
  } @ inputs: let
    inherit (self) outputs;

    systems = [
      "aarch64-linux"
      "x86_64-linux"
    ];
    forAllSystems = nixpkgs.lib.genAttrs systems;
  in {
    formatter = forAllSystems (system: nixpkgs.legacyPackages.${system}.alejandra);

    nixpkgs.overlays = [inputs.niri.overlays.niri];

    nixosConfigurations = {
      desktop = nixpkgs.lib.nixosSystem {
        specialArgs = {inherit inputs outputs;};
        modules = [
          home-manager.nixosModules.home-manager
          dotfiles-private.nixosModules.default
          niri-flake.nixosModules.niri
          ./hosts/desktop/configuration.nix
        ];
      };

      laptop = nixpkgs.lib.nixosSystem {
        specialArgs = {inherit inputs outputs;};
        modules = [
          home-manager.nixosModules.home-manager
          dotfiles-private.nixosModules.default
          disko.nixosModules.disko
          niri-flake.nixosModules.niri
          ./hosts/laptop/configuration.nix
        ];
      };

      # build with:
      # nix build .#nixosConfigurations.installer.config.system.build.isoImage
      installer = nixpkgs.lib.nixosSystem {
        specialArgs = {inherit inputs outputs;};
        modules = [
          ./hosts/installer/configuration.nix
        ];
      };
    };
  };
}
