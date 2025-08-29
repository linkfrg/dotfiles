{
  config,
  lib,
  ...
}: let
  cfg = config.custom.core.nix;
in {
  options.custom.core.nix = {
    enable = lib.mkEnableOption "Enable Nix & nixpkgs settings";
  };

  config = lib.mkIf cfg.enable {
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
}
