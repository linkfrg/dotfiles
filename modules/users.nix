{self, ...}: {
  flake.nixosModules.linkUser = {pkgs, ...}: {
    users.users.link = {
      isNormalUser = true;
      shell = pkgs.fish;
      extraGroups = [
        "wheel"
        "input"
        "libvirtd"
        "docker"
        "networkmanager"
      ];
    };

    home-manager.users.link = self.homeModules.linkModule;
  };
}
