{inputs, ...}: {
  flake.nixosModules.sops = {pkgs, ...}: let
    owner = "link";
  in {
    imports = [
      inputs.sops-nix.nixosModules.sops
    ];

    environment.systemPackages = with pkgs; [
      age
      sops
    ];

    sops = {
      age.keyFile = "/home/link/.config/sops/age/keys.txt";
      defaultSopsFile = ../secrets.yaml;
      defaultSopsFormat = "yaml";

      secrets = {
        "ssh/github/public" = {inherit owner;};
        "ssh/github/private" = {inherit owner;};
      };
    };
  };
}
