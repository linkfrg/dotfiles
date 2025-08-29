{
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.terminal.micro;
in {
  options.custom.terminal.micro = {
    enable = lib.mkEnableOption "Enable micro";
  };

  config = lib.mkIf cfg.enable {
    environment.systemPackages = with pkgs; [
      micro
    ];

    environment.variables.EDITOR = "micro";
  };
}
