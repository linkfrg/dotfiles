{pkgs, ...}: {
  home.packages = with pkgs; [
    prismlauncher
    osu-lazer-bin
  ];
}
