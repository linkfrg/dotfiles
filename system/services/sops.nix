{pkgs, ...}: let
  owner = "link";
in {
  environment.systemPackages = with pkgs; [
    age
    sops
  ];

  sops = {
    age.keyFile = "/home/link/.config/sops/age/keys.txt";
    defaultSopsFile = ../../secrets/secrets.yaml;
    defaultSopsFormat = "yaml";

    secrets = {
      "ssh/github/public" = {inherit owner;};
      "ssh/github/private" = {inherit owner;};
    };
  };
}
