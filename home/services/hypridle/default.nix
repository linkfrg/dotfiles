let
  on_cmd = "~/.config/hypr/monitor-switch.sh on";
  off_cmd = "~/.config/hypr/monitor-switch.sh off";
in {
  home.file = {
    ".config/hypr/monitor-switch.sh".source = ./monitor-switch.sh;
  };

  services.hypridle = {
    enable = true;

    settings = {
      general = {
        lock_cmd = "hyprlock";

        before_sleep_cmd = "hyprlock";
        after_sleep_cmd = on_cmd;
      };
      listener = [
        {
          timeout = 180;
          on-timeout = off_cmd;
          on-resume = on_cmd;
        }
        {
          timeout = 600;
          on-timeout = "hyprlock";
        }
      ];
    };
  };
}
