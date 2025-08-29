{
  config,
  lib,
  ...
}: let
  cfg = config.custom.core;
in {
  imports = [
    ./bootloader.nix
    ./locale.nix
    ./networking.nix
    ./users.nix
  ];

  options.custom.core = {
    enable = lib.mkEnableOption "Enable core settings";
  };

  config = lib.mkIf cfg.enable {
    nixpkgs = {
      config = {
        allowUnfree = true;
      };
    };

    nix = {
      settings = {
        experimental-features = "nix-command flakes";
        flake-registry = "";
        nix-path = "";
      };
      channel.enable = false;
    };

    system.stateVersion = "25.05";
  };
}
