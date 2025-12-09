{pkgs, ...}: {
  programs.thunar = {
    enable = true;
    plugins = with pkgs.xfce; [
      thunar-archive-plugin
    ];
  };

  environment.systemPackages = with pkgs; [
    file-roller
  ];

  services.gvfs.enable = true;
  services.tumbler.enable = true;
}
