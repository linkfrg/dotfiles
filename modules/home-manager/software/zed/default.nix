{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.software.zed;
in {
  options.custom.software.zed = {
    enable = lib.mkEnableOption "Enable kitty";
  };

  config = lib.mkIf cfg.enable {
    programs.zed-editor = {
      enable = true;

      extraPackages = with pkgs; [
        nil
        alejandra
        rust-analyzer
      ];

      extensions = import ./extensions.nix;
      themes = import ./themes.nix;
      userSettings = import ./settings.nix;
      userKeymaps = import ./keymaps.nix;
    };
  };
}
