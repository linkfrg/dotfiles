{
  programs.fish = {
    enable = true;
    interactiveShellInit = ''
      set -g fish_greeting
      set --global fish_color_command blue
    '';
  };

  programs.man.generateCaches = false; # speed up building
}
