{
  programs.fastfetch = {
    enable = true;

    settings = {
      logo = {
        type = "small";
      };

      general = {
        detectVersion = false;
      };

      modules = [
        "title"
        {
          type = "os";
          format = "{name}";
        }
        "packages"
        "shell"
        {
          type = "wm";
          format = "{pretty-name}";
        }
        "terminal"
        "memory"
      ];
    };
  };
}
