{pkgs, ...}: {
  programs.thunar = {
    enable = true;
    plugins = with pkgs.xfce; [
      thunar-archive-plugin
    ];
  };

  programs.file-roller.enable = true;
  services.gvfs.enable = true;
  services.tumbler.enable = true;
}
