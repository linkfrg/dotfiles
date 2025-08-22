{
  config,
  lib,
  ...
}: let
  cfg = config.custom.desktop.hyprlock;
in {
  options.custom.desktop.hyprlock = {
    enable = lib.mkEnableOption "Enable hyprlock";
  };

  config = lib.mkIf cfg.enable {
    home.file = {
      ".config/hypr/hyprlock-time.sh".source = ./hyprlock-time.sh;
    };
    programs.hyprlock = {
      enable = true;

      settings = {
        source = ["~/.cache/ignis/material/dark_colors-hyprland.conf"];

        # BACKGROUND
        background = {
          monitor = "";
          path = "~/.local/share/ignis/wallpaper";
          blur_passes = "2";
          contrast = "0.9";
          brightness = "0.5";
          vibrancy = "0.17";
          vibrancy_darkness = "0";
        };

        # GENERAL
        general = {
          disable_loading_bar = true;
        };

        # INPUT FIELD
        input-field = {
          monitor = "";
          size = "300, 40";
          outline_thickness = "2";
          dots_size = "0.2"; # Scale of input-field height, 0.2 - 0.8
          dots_spacing = "0.2"; # Scale of dots' absolute size, 0.0 - 1.0
          dots_center = true;
          outer_color = "$surface";
          inner_color = "$surface";
          font_color = "$onSurface";
          fade_on_empty = false;
          placeholder_text = "";
          hide_input = false;
          position = "0, 150";
          halign = "center";
          valign = "bottom";
        };

        # Hour-Time
        label = [
          {
            monitor = "";
            text = "cmd[update:1000] echo -e \"$(date +\"%H\")\"";
            color = "$primary";
            font_family = "JetBrainsMono Bold";
            font_size = "180";
            position = "0, 150";
            halign = "center";
            valign = "center";
          }

          # Minute-Time
          {
            monitor = "";
            text = "cmd[update:1000] echo -e \"$(date +\"%M\")\"";
            color = "$onSurface";
            font_family = "JetBrainsMono Bold";
            font_size = "180";
            position = "0, -75";
            halign = "center";
            valign = "center";
          }

          # Date
          {
            monitor = "";
            text = "cmd[update:1000] echo -e \"$(date +\"%a, %b %d\")\"";
            color = "$onSurface";
            font_family = "JetBrainsMono Bold";
            position = "100, -100";
            halign = "left";
            valign = "top";
          }

          # Date
          {
            monitor = "";
            text = "cmd[update:1000] primaryHex=$primaryHex bash ~/.config/hypr/hyprlock-time.sh";
            color = "$onSurface";
            font_family = "JetBrainsMono Bold";
            position = "100, -130";
            halign = "left";
            valign = "top";
          }
        ];
      };
    };
  };
}
