{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.terminal.starship;
in {
  options.linkfrg-dotfiles.terminal.starship = {
    enable = lib.mkEnableOption "Enable starship";
  };

  config = lib.mkIf cfg.enable {
    programs.starship = {
      enable = true;
      enableFishIntegration = true;
      settings = {
        add_newline = false;
        format = builtins.concatStringsSep "" [
          "$os"
          "$directory"
          "$git_branch"
          "$git_status"
          "$fill"
          "$python"
          "\n$character"
        ];
        character = {
          success_symbol = "[❯](bold green)";
          error_symbol = "[✗](bold red)";
        };

        fill = {
          symbol = " ";
        };
      };
    };
  };
}
