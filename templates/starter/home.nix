{inputs, ...}: {
  imports = [
    inputs.linkfrg-dotfiles.homeManagerModules.public
  ];

  linkfrg-dotfiles = {
    hyprland.enable = true;
    hyprlock.enable = true;
    ignis.enable = true;
    kitty.enable = true;
  };

  # FIXME: replace "username" with your username
  home = {
    username = "username";
    homeDirectory = "/home/username";
  };

  nixpkgs = {
    config = {
      allowUnfree = true;
    };
  };

  programs.home-manager.enable = true;
  home.stateVersion = "25.05";
}
