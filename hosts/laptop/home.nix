{
  imports = [
    ../common/home.nix
  ];

  linkfrg-dotfiles = {
    terminal = {
      nvtop = {
        enable = true;
        intel = true;
      };
    };
  };
}
