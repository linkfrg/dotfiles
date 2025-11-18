{pkgs, ...}: {
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
}
