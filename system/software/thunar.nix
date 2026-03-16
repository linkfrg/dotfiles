{pkgs, ...}: {
  programs.thunar = {
    enable = true;
    plugins = with pkgs; [
      thunar-archive-plugin
    ];
  };

  environment.systemPackages = with pkgs; [
    file-roller
  ];

  services.gvfs.enable = true;
  services.tumbler.enable = true;
}
