{
  flake.homeModules.niri = {
    pkgs,
    lib,
    config,
    ...
  }: {
    home.packages = with pkgs; [
      xwayland-satellite
      sway-contrib.grimshot
    ];

    xdg.portal = {
      enable = true;
      xdgOpenUsePortal = true;
      config = {
        common = {
          default = [
            "gtk"
            "gnome"
          ];
        };
        niri = {
          default = [
            "gtk"
            "gnome"
          ];
        };
      };
    };
    xdg.portal.extraPortals = [
      pkgs.xdg-desktop-portal-gnome
      pkgs.xdg-desktop-portal-gtk
    ];

    services.polkit-gnome.enable = true;

    programs.niri = {
      settings = lib.mkMerge [
        (import ./_binds.nix {inherit config;})
        ./_input.nix
        ./_layout.nix
        ./_misc.nix
        ./_rules.nix
        ./_spawn.nix
        ./_env.nix
      ];
    };
  };
}
