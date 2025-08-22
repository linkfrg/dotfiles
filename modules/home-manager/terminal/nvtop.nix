{
  config,
  lib,
  pkgs,
  ...
}: let
  cfg = config.linkfrg-dotfiles.terminal.nvtop;
in {
  options.linkfrg-dotfiles.terminal.nvtop = {
    enable = lib.mkEnableOption "Enable nvtop";
    nvidia = lib.mkEnableOption "Enable for nvidia";
    intel = lib.mkEnableOption "Enable for intel";
  };

  config = lib.mkIf cfg.enable (
    lib.mkMerge [
      (lib.mkIf cfg.nvidia {
        home.packages = with pkgs; [
          nvtopPackages.nvidia
        ];
      })
      (lib.mkIf cfg.intel {
        home.packages = with pkgs; [
          nvtopPackages.intel
        ];
      })
    ]
  );
}
