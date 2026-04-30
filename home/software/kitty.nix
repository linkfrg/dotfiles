{pkgs, ...}: {
  programs.kitty = {
    enable = true;
    font = {
      package = pkgs.nerd-fonts.jetbrains-mono;
      size = 12;
      name = "JetBrainsMono Nerd Font Mono";
    };
    settings = {
      include = "~/.cache/ignis/material/dark_colors-kitty.conf";
      window_margin_width = 15;
      remember_window_size = "no";
      background_opacity = 1;
    };
  };
}
