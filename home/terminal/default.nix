{ pkgs, ... }:
{
  imports = [
    ./starship.nix
    ./fastfetch.nix
  ];

  programs.btop.enable = true;

  programs.direnv = {
    enable = true;
    # enableFishIntegration = true;
    nix-direnv.enable = true;
    silent = true;
  };

  programs.fish = {
    enable = true;
    interactiveShellInit = ''
      set -g fish_greeting
      set --global fish_color_command blue
    '';
  };

  programs.git = {
    enable = true;

    settings = {
      user = {
        name = "Link";
        email = "linkfrg.dev@proton.me";
      };

      init.defaultBranch = "main";
    };
  };

  programs.man.generateCaches = false; # speed up building
  home.packages = with pkgs; [
    cmatrix
    cava
    gh
    speedtest-cli
    yazi
    cloc
    act
    wl-clipboard
    tmux
  ];
}
