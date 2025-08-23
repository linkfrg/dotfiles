{
  "$mainMod" = "SUPER";
  "$ignisCli" = "ignisctl-rs";
  bind =
    [
      "$mainMod, C, killactive"
      "$mainMod SHIFT, M, exit"
      "$mainMod, V, togglefloating"
      "$mainMod, P, pseudo"
      "$mainMod, J, togglesplit"
      ",F11, fullscreen, 0"
      "$mainMod, G, centerwindow"
      "$mainMod, D, pin"

      "$mainMod, X, exec, $ignisCli toggle-window ignis_LAUNCHER"
      "$mainMod, M, exec, $ignisCli toggle-window ignis_POWERMENU"
      "ALT, F4, exec, $ignisCli toggle-window ignis_POWERMENU"

      "$mainMod, Q, exec, kitty"
      "$mainMod, L, exec, hyprlock"
      "$mainMod, E, exec, thunar"
      "$mainMod SHIFT, S, exec, GRIMBLAST_HIDE_CURSOR=0 grimblast --notify --freeze copysave area"
      "$mainMod, S, exec, GRIMBLAST_HIDE_CURSOR=0 grimblast --notify --freeze copysave output"
      ",PRINT, exec, GRIMBLAST_HIDE_CURSOR=0 grimblast --notify --freeze copysave output"

      "$mainMod, left, movefocus, l"
      "$mainMod, right, movefocus, r"
      "$mainMod, up, movefocus, u"
      "$mainMod, down, movefocus, d"

      "$mainMod, mouse_down, workspace, e+1"
      "$mainMod, mouse_up, workspace, e-1"

      "$mainMod, 0, workspace, 10"
      "$mainMod SHIFT, 0, movetoworkspace, 10"

      ",XF86AudioRaiseVolume, exec, pamixer -i 5 && $ignisCli open-window ignis_OSD"
      ",XF86AudioLowerVolume, exec, pamixer -d 5 && $ignisCli open-window ignis_OSD"
      ",XF86AudioMute, exec, pamixer -t && $ignisCli open-window ignis_OSD"
    ]
    ++ (
      # workspaces
      # binds $mod + [shift +] {1..9} to [move to] workspace {1..9}
      builtins.concatLists (
        builtins.genList (
          i: let
            ws = i + 1;
          in [
            "$mainMod, code:1${toString i}, workspace, ${toString ws}"
            "$mainMod SHIFT, code:1${toString i}, movetoworkspace, ${toString ws}"
          ]
        )
        9
      )
    );

  bindm = [
    "$mainMod, mouse:272, movewindow"
    "$mainMod, mouse:273, resizewindow"
  ];
}
