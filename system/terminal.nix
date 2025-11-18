{pkgs, ...}: {
  environment.systemPackages = with pkgs; [
    usbutils
    libva-utils
    tree
    file
    f2fs-tools
    micro
    gnome-disk-utility
  ];

  programs.fish = {
    enable = true;
    interactiveShellInit = ''
      set -g fish_greeting
      set --global fish_color_command blue
    '';
  };

  documentation.man.generateCaches = false; # speed up building

  environment.variables.EDITOR = "micro";
}
