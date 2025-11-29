{config, ...}: {
  binds = with config.lib.niri.actions; {
    "Mod+Q".action = spawn "kitty";
    "Mod+X".action = spawn "ignisctl-rs" "open-window" "ignis_LAUNCHER";
    "Mod+L".action = spawn "hyprlock";
    "Mod+E".action = spawn "thunar";

    XF86AudioRaiseVolume = {
      allow-when-locked = true;
      action = spawn "ignisctl-rs" "run-command" "volume-osd-increase";
    };
    XF86AudioLowerVolume = {
      allow-when-locked = true;
      action = spawn "ignisctl-rs" "run-command" "volume-osd-decrease";
    };
    XF86AudioMute = {
      allow-when-locked = true;
      action = spawn "ignisctl-rs" "run-command" "volume-osd-toggle-mute";
    };
    # XF86AudioMicMute     allow-when-locked=true { spawn-sh "wpctl set-mute @DEFAULT_AUDIO_SOURCE@ toggle"; }

    # // Example brightness key mappings for brightnessctl.
    # // You can use regular spawn with multiple arguments too (to avoid going through "sh"),
    # // but you need to manually put each argument in separate "" quotes.
    # XF86MonBrightnessUp allow-when-locked=true { spawn "brightnessctl" "--class=backlight" "set" "+10%"; }
    # XF86MonBrightnessDown allow-when-locked=true { spawn "brightnessctl" "--class=backlight" "set" "10%-"; }

    "Mod+C" = {
      action = close-window;
      repeat = false;
    };

    "Mod+W".action = focus-window-or-workspace-up;
    "Mod+A".action = focus-column-left;
    "Mod+S".action = focus-window-or-workspace-down;
    "Mod+D".action = focus-column-right;

    "Mod+Ctrl+W".action = move-column-to-workspace-up;
    "Mod+Ctrl+A".action = move-column-left;
    "Mod+Ctrl+S".action = move-column-to-workspace-down;
    "Mod+Ctrl+D".action = move-column-right;

    "Mod+Alt+W".action = focus-monitor-up;
    "Mod+Alt+A".action = focus-monitor-left;
    "Mod+Alt+S".action = focus-monitor-down;
    "Mod+Alt+D".action = focus-monitor-right;

    "Mod+Alt+Ctrl+W".action = move-column-to-monitor-up;
    "Mod+Alt+Ctrl+A".action = move-column-to-monitor-left;
    "Mod+Alt+Ctrl+S".action = move-column-to-monitor-down;
    "Mod+Alt+Ctrl+D".action = move-column-to-monitor-right;

    "Mod+grave".action = toggle-overview;
    "Mod+G".action = consume-or-expel-window-left;
    "Mod+H".action = consume-or-expel-window-right;

    "Mod+Shift+G".action = consume-window-into-column;
    "Mod+Shift+H".action = expel-window-from-column;

    "Mod+R".action = switch-preset-column-width;
    "Mod+Shift+R".action = switch-preset-window-height;
    "Mod+Ctrl+R".action = reset-window-height;

    "Mod+F".action = maximize-column;
    "Mod+Shift+F".action = fullscreen-window;
    "Mod+Ctrl+F".action = expand-column-to-available-width;

    "Mod+Shift+Minus".action = set-window-height "-10%";
    "Mod+Shift+Equal".action = set-window-height "+10%";

    "Mod+V".action = toggle-window-floating;
    "Mod+Shift+V".action = switch-focus-between-floating-and-tiling;

    "Print".action = spawn "grimshot" "--notify" "savecopy" "output";
    "Mod+Shift+S".action = spawn "grimshot" "--notify" "savecopy" "area";

    "Mod+Escape" = {
      allow-inhibiting = false;
      action = toggle-keyboard-shortcuts-inhibit;
    };

    "Ctrl+Alt+Delete".action = quit;
  };
}
