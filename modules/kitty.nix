{
  flake.homeModules.kitty = {pkgs, ...}: {
    home.packages = with pkgs; [
      kitty
      nerd-fonts.jetbrains-mono
    ];

    xdg.configFile."kitty".source = ../config/kitty;

    programs.fish.interactiveShellInit = ''
      if set -q KITTY_INSTALLATION_DIR
          set --global KITTY_SHELL_INTEGRATION enabled
          source "$KITTY_INSTALLATION_DIR/shell-integration/fish/vendor_conf.d/kitty-shell-integration.fish"
          set --prepend fish_complete_path "$KITTY_INSTALLATION_DIR/shell-integration/fish/vendor_completions.d"
      end
    '';
  };
}
