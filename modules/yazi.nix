{
  flake.homeModules.yazi =
    {
      pkgs,
      config,
      lib,
      ...
    }:
    {
      programs.yazi = {
        enable = true;
        enableFishIntegration = true;
        shellWrapperName = "y";
        plugins = {
            inherit (pkgs.yaziPlugins) mount;
            inherit (pkgs.yaziPlugins) wl-clipboard;
        };

        settings = {
          theme = lib.importTOML ../config/yazi/theme.toml;
          keymap = lib.importTOML ../config/yazi/keymap.toml;
        };
      };
    };
}
