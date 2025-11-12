{config, ...}: {
  binds = with config.lib.niri.actions; {
    "Mod+Shift+Slash".action = show-hotkey-overlay;

    "Mod+Q".action = spawn "kitty";
    "Mod+X".action = spawn "ignisctl-rs" "open-window" "ignis_LAUNCHER";
    "Mod+L".action = spawn "hyprlock";
    "Mod+E".action = spawn "thunar";

    XF86AudioRaiseVolume = {
      allow-when-locked = true;
      action = spawn "pamixer" "-i" "5";
    };
    XF86AudioLowerVolume = {
      allow-when-locked = true;
      action = spawn "pamixer" "-d" "5";
    };
    XF86AudioMute = {
      allow-when-locked = true;
      action = spawn "pamixer" "-t";
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

    "Mod+Shift+W".action = move-window-up;
    "Mod+Shift+A".action = move-column-left;
    # "Mod+Shift+S".action = move-window-down;
    "Mod+Shift+D".action = move-column-right;

    "Mod+grave".action = toggle-overview;

    "Mod+Home".action = focus-column-first;
    "Mod+End".action = focus-column-last;
    "Mod+Shift+Home".action = move-column-to-first;
    "Mod+Shift+End".action = move-column-to-last;

    # Mod+Shift+Left  { focus-monitor-left; }
    # Mod+Shift+Down  { focus-monitor-down; }
    # Mod+Shift+Up    { focus-monitor-up; }
    # Mod+Shift+Right { focus-monitor-right; }
    # Mod+Shift+H     { focus-monitor-left; }
    # Mod+Shift+J     { focus-monitor-down; }
    # Mod+Shift+K     { focus-monitor-up; }
    # Mod+Shift+L     { focus-monitor-right; }

    # Mod+Shift+Ctrl+Left  { move-column-to-monitor-left; }
    # Mod+Shift+Ctrl+Down  { move-column-to-monitor-down; }
    # Mod+Shift+Ctrl+Up    { move-column-to-monitor-up; }
    # Mod+Shift+Ctrl+Right { move-column-to-monitor-right; }
    # Mod+Shift+Ctrl+H     { move-column-to-monitor-left; }
    # Mod+Shift+Ctrl+J     { move-column-to-monitor-down; }
    # Mod+Shift+Ctrl+K     { move-column-to-monitor-up; }
    # Mod+Shift+Ctrl+L     { move-column-to-monitor-right; }

    # // Alternatively, there are commands to move just a single window:
    # // Mod+Shift+Ctrl+Left  { move-window-to-monitor-left; }
    # // ...

    # // And you can also move a whole workspace to another monitor:
    # // Mod+Shift+Ctrl+Left  { move-workspace-to-monitor-left; }
    # // ...

    # Mod+Page_Down      { focus-workspace-down; }
    # Mod+Page_Up        { focus-workspace-up; }
    # Mod+U              { focus-workspace-down; }
    # Mod+I              { focus-workspace-up; }
    # Mod+Ctrl+Page_Down { move-column-to-workspace-down; }
    # Mod+Ctrl+Page_Up   { move-column-to-workspace-up; }
    # Mod+Ctrl+U         { move-column-to-workspace-down; }
    # Mod+Ctrl+I         { move-column-to-workspace-up; }

    # // Alternatively, there are commands to move just a single window:
    # // Mod+Ctrl+Page_Down { move-window-to-workspace-down; }
    # // ...

    # Mod+Shift+Page_Down { move-workspace-down; }
    # Mod+Shift+Page_Up   { move-workspace-up; }
    # Mod+Shift+U         { move-workspace-down; }
    # Mod+Shift+I         { move-workspace-up; }

    # // You can bind mouse wheel scroll ticks using the following syntax.
    # // These binds will change direction based on the natural-scroll setting.
    # //
    # // To avoid scrolling through workspaces really fast, you can use
    # // the cooldown-ms property. The bind will be rate-limited to this value.
    # // You can set a cooldown on any bind, but it's most useful for the wheel.
    # Mod+WheelScrollDown      cooldown-ms=150 { focus-workspace-down; }
    # Mod+WheelScrollUp        cooldown-ms=150 { focus-workspace-up; }
    # Mod+Ctrl+WheelScrollDown cooldown-ms=150 { move-column-to-workspace-down; }
    # Mod+Ctrl+WheelScrollUp   cooldown-ms=150 { move-column-to-workspace-up; }

    # Mod+WheelScrollRight      { focus-column-right; }
    # Mod+WheelScrollLeft       { focus-column-left; }
    # Mod+Ctrl+WheelScrollRight { move-column-right; }
    # Mod+Ctrl+WheelScrollLeft  { move-column-left; }

    # // Usually scrolling up and down with Shift in applications results in
    # // horizontal scrolling; these binds replicate that.
    # Mod+Shift+WheelScrollDown      { focus-column-right; }
    # Mod+Shift+WheelScrollUp        { focus-column-left; }
    # Mod+Ctrl+Shift+WheelScrollDown { move-column-right; }
    # Mod+Ctrl+Shift+WheelScrollUp   { move-column-left; }

    "Mod+1".action = focus-workspace 1;
    "Mod+2".action = focus-workspace 2;
    "Mod+3".action = focus-workspace 3;
    "Mod+4".action = focus-workspace 4;
    "Mod+5".action = focus-workspace 5;
    "Mod+6".action = focus-workspace 6;
    "Mod+7".action = focus-workspace 7;
    "Mod+8".action = focus-workspace 8;
    "Mod+9".action = focus-workspace 9;
    # "Mod+Shift+1".action = move-window-to-workspace 1;
    # "Mod+Shift+2".action = move-window-to-workspace 2;
    # "Mod+Shift+3".action = move-window-to-workspace 3;
    # "Mod+Shift+4".action = move-window-to-workspace 4;
    # "Mod+Shift+5".action = move-window-to-workspace 5;
    # "Mod+Shift+6".action = move-window-to-workspace 6;
    # "Mod+Shift+7".action = move-window-to-workspace 7;
    # "Mod+Shift+8".action = move-window-to-workspace 8;
    # "Mod+Shift+9".action = move-window-to-workspace 9;

    "Mod+G".action = consume-or-expel-window-left;
    "Mod+H".action = consume-or-expel-window-right;

    "Mod+Shift+G".action = consume-window-into-column;
    "Mod+Shift+H".action = expel-window-from-column;

    "Mod+R".action = switch-preset-column-width;
    # // Cycling through the presets in reverse order is also possible.
    # // Mod+R { switch-preset-column-width-back; }
    "Mod+Shift+R".action = switch-preset-window-height;
    "Mod+Ctrl+R".action = reset-window-height;
    "Mod+F".action = maximize-column;
    "Mod+Shift+F".action = fullscreen-window;

    # // Expand the focused column to space not taken up by other fully visible columns.
    # // Makes the column "fill the rest of the space".
    "Mod+Ctrl+F".action = expand-column-to-available-width;

    # Mod+C { center-column; }

    # // Center all fully visible columns on screen.
    # Mod+Ctrl+C { center-visible-columns; }

    "Mod+Shift+Minus".action = set-window-height "-10%";
    "Mod+Shift+Equal".action = set-window-height "+10%";

    "Mod+V".action = toggle-window-floating;
    "Mod+Shift+V".action = switch-focus-between-floating-and-tiling;

    # // Toggle tabbed column display mode.
    # // Windows in this column will appear as vertical tabs,
    # // rather than stacked on top of each other.
    "Mod+T".action = toggle-column-tabbed-display;

    "Print".action = spawn "grimshot" "--notify" "savecopy" "output";
    "Mod+Shift+S".action = spawn "grimshot" "--notify" "savecopy" "area";
    # Ctrl+Print { screenshot-screen; }
    # Alt+Print { screenshot-window; }

    # // Applications such as remote-desktop clients and software KVM switches may
    # // request that niri st here
    # // so they may, for example, forward the key presses as-is to a remote machine.
    # // It's a good idea to bind an escape hatch to toggle the inhibitor,
    # // so a buggy application can't hold your session hostage.
    # //
    # // The allow-inhibiting=false property can be applied to other binds as well,
    # // which ensures niri always processes them, even when an inhibitor is active.
    # Mod+Escape allow-inhibiting=false { toggle-keyboard-shortcuts-inhibit; }

    # // The quit action will show a confirmation dialog to avoid accidental exits.
    # Mod+Shift+E { quit; }
    "Ctrl+Alt+Delete".action = quit;

    # // Powers off the monitors. To turn them back on, do any input like
    # // moving the mouse or pressing any other key.
    # Mod+Shift+P { power-off-monitors; }
  };
}
