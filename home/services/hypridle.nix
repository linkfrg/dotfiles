{
  services.hypridle = {
    enable = true;

    settings = {
      general = {
        lock_cmd = "hyprlock";

        before_sleep_cmd = "hyprlock";
        after_sleep_cmd = "hyprctl dispatch dpms on";
      };
      listener = [
        {
          timeout = 180;
          on-timeout = "hyprctl dispatch dpms off";
          on-resume = "hyprctl dispatch dpms on";
        }
        {
          timeout = 600;
          on-timeout = "hyprlock";
        }
      ];
    };
  };
}
