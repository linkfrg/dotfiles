{
  flake.nixosModules.niri =
    { pkgs, ... }:
    {
      programs.niri = {
        enable = true;
        package = pkgs.niri;
      };
    };

  flake.homeModules.niri =
    {
      pkgs,
      lib,
      config,
      ...
    }:
    {
      home.packages = with pkgs; [
        xwayland-satellite
        sway-contrib.grimshot
      ];

      xdg.portal = {
        enable = true;
        # xdgOpenUsePortal = true;
        config.common.default = [ "gnome" ];
        extraPortals = [
          pkgs.xdg-desktop-portal-gnome
          pkgs.xdg-desktop-portal-gtk
        ];

      };

      services.polkit-gnome.enable = true;

      xdg.configFile."niri/config.kdl".source = ../config/niri/config.kdl;
    };
}
