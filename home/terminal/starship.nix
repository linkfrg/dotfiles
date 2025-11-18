{
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
}
