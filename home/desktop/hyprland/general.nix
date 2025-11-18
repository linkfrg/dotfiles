{
  cursor = {
    no_hardware_cursors = true;
  };

  input = {
    kb_options = "grp:win_space_toggle";
    accel_profile = "flat";

    follow_mouse = 1;

    touchpad = {
      natural_scroll = "yes";
    };

    sensitivity = 0;
  };

  general = {
    gaps_in = 5;
    gaps_out = 20;
    border_size = 2;
    resize_on_border = true;
    layout = "dwindle";
  };

  decoration = {
    rounding = 15;

    blur = {
      enabled = true;
      size = 12;
      passes = 4;
      new_optimizations = true;
    };

    shadow = {
      enabled = true;
      range = 30;
      render_power = 4;
      color = "rgb(000000)";
    };
  };

  animations = {
    enabled = "yes";

    bezier = "quart, 0.25, 1, 0.5, 1";

    animation = [
      "windows, 1, 6, quart, slide"
      "border, 1, 6, quart"
      "borderangle, 1, 6, quart"
      "fade, 1, 6, quart"
      "workspaces, 1, 6, quart"
    ];
  };

  dwindle = {
    pseudotile = "yes";
    preserve_split = "yes";
  };

  misc = {
    disable_hyprland_logo = true;
    enable_anr_dialog = false;
  };
}
