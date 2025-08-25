{
  icon_theme = "Material Icon Theme";
  buffer_font_family = "JetBrains Mono";
  minimap = {
    show = "always";
  };
  ui_font_size = 16;
  buffer_font_size = 14;
  theme = {
    mode = "dark";
    light = "Catppuccin Mocha (blue)";
    dark = "Catppuccin Mocha (blue)";
  };
  tabs = {
    file_icons = true;
  };
  languages = {
    Python = {
      language_servers = [
        "ruff"
        "pyright"
      ];
      format_on_save = "on";
    };
    Nix = {
      format_on_save = "on";
      language_servers = [
        "nil"
        "!nixd"
      ];
      formatter = {
        external = {
          command = "alejandra";
          arguments = [
            "--quiet"
            "--"
          ];
        };
      };
    };
  };
  terminal = {
    detect_venv = {
      on = {
        activate_script = "fish";
      };
    };
    dock = "bottom";
  };
  lsp = {
    pyright = {
      settings = {
        "python.analysis" = {
          # turn off hysteria
          typeCheckingMode = "off";
        };
      };
    };
  };
}
