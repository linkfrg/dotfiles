{pkgs, ...}: {
  programs.btop.enable = true;
  home.packages = with pkgs; [
    cmatrix
    cava
    gh
    speedtest-cli
    yazi
    cloc
    act
  ];

  programs.direnv = {
    enable = true;
    # enableFishIntegration = true;
    nix-direnv.enable = true;
    silent = true;
  };
}
