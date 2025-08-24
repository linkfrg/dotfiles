{
  inputs,
  outputs,
  ...
}: {
  imports = [
    outputs.homeManagerModules.default
    outputs.homeManagerModules.public
    inputs.dotfiles-private.homeManagerModules.default
  ];

  linkfrg-dotfiles = {
    hyprland.enable = true;
    hyprlock.enable = true;
    ignis.enable = true;
    kitty.enable = true;
    xdgPortal.enable = true;
  };

  custom = {
    core = {
      enable = true;
      username = "link";
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
