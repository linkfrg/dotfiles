{
  windowrule = [
    "float, class:pavucontrol"
    "pin, class:pavucontrol"
    "size 900 500, class:pavucontrol"

    "float, class:kitty"
    "size 640 400, class:kitty"

    "float,class:^(Material Settings)$"
  ];

  layerrule = [
    "blur,^(ignis_BAR.*)$"
    "noanim,^(ignis_NOTIFICATION_POPUP.*)$"
    "noanim,^(ignis_CONTROL_CENTER.*)$"
  ];
}
