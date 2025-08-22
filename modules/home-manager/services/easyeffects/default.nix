{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.services.easyeffects;

  loadPreset = path: builtins.fromJSON (builtins.readFile path);
in {
  options.linkfrg-dotfiles.services.easyeffects = {
    enable = lib.mkEnableOption "Enable easyeffects service";
  };

  config = lib.mkIf cfg.enable {
    services.easyeffects = {
      enable = true;
      preset = "main";
      extraPresets = {
        main = loadPreset ./output/main.json;
      };
    };
  };
}
