{inputs, config, lib, pkgs, ...}: let
  cfg = config.custom.desktop.niri;
in {
  imports = [
    inputs.niri-flake.nixosModules.niri
  ];

  options.custom.desktop.niri = {
    enable = lib.mkEnableOption "Enable niri";
  };

  config = lib.mkIf cfg.enable {
    programs.niri = {
      enable = true;
      package = pkgs.niri;
    };
  };
}
