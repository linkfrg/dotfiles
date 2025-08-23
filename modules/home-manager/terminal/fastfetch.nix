{
  config,
  lib,
  ...
}: let
  cfg = config.custom.terminal.fastfetch;
in {
  options.custom.terminal.fastfetch = {
    enable = lib.mkEnableOption "Enable fastfetch";
  };

  config = lib.mkIf cfg.enable {
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
  };
}
