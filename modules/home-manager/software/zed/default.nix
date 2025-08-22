{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.software.zed;
in {
  options.linkfrg-dotfiles.software.zed = {
    enable = lib.mkEnableOption "Enable kitty";
  };

  config = lib.mkIf cfg.enable {
    programs.zed-editor = {
      enable = true;

      extraPackages = with pkgs; [
        nil
        alejandra
      ];

      extensions = import ./extensions.nix;
      themes = import ./themes.nix;
      userSettings = import ./settings.nix;
      userKeymaps = import ./keymaps.nix;
    };
  };
}
