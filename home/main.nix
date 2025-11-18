{
  home = {
    username = "link";
    homeDirectory = "/home/link";
  };

  nixpkgs.config.allowUnfree = true;

  programs.home-manager.enable = true;

  home.stateVersion = "25.05";
}
