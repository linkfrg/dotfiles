{
  inputs,
  outputs,
  ...
}: {
  imports = [
    outputs.homeManagerModules.default
    inputs.dotfiles-private.homeManagerModules.default
  ];

  custom = {
    core = {
      enable = true;
      username = "link";
    };

    desktop = {
      hyprland.enable = true;
      hyprlock.enable = true;
      ignis.enable = true;
      waylandEnv.enable = true;
      xdgPortal.enable = true;
    };

    services = {
      easyeffects.enable = true;
      xdgUserDirs.enable = true;
    };

    software = {
      firefox = {
        enable = true;
      };
      zed.enable = true;
      chromium.enable = true;
      common.enable = true;
      gtk.enable = true;
      kitty.enable = true;
    };

    terminal = {
      btop.enable = true;
      develop.enable = true;
      direnv.enable = true;
      fastfetch.enable = true;
      fish.enable = true;
      git.enable = true;
      starship.enable = true;
    };

    theming = {
      cursorTheme.enable = true;
      fonts.enable = true;
      iconTheme.enable = true;
    };
  };

  gtk.gtk3.bookmarks = [
    "file:///data"
    "file:///data/ignis"
    "file:///data/dotfiles"
  ];

  wayland.windowManager.hyprland.settings = {
    exec-once = [
      "Telegram -startintray"
    ];

    input = {
      kb_layout = "us, ru";
    };
  };
}
