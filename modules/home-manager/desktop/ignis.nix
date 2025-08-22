{
  self,
  inputs,
  pkgs,
  config,
  lib,
  ...
}: let
  cfg = config.custom.desktop.ignis;
in {
  imports = [inputs.ignis.homeManagerModules.default];

  options.custom.desktop.ignis = {
    enable = lib.mkEnableOption "Enable Ignis";
  };

  config = lib.mkIf cfg.enable {
    home.packages = with pkgs; [
      pamixer
      inputs.ignisctl-rs.packages.${system}.ignisctl-rs
    ];

    home.file = {
      ".local/share/themes/Material".source = "${self}/Material";
    };

    programs.ignis = {
      enable = true;

      addToPythonEnv = true;
      configDir = "${self}/ignis";

      services = {
        bluetooth.enable = true;
        recorder.enable = true;
        audio.enable = true;
        network.enable = true;
      };

      sass = {
        enable = true;
        useDartSass = true;
      };

      extraPackages = with pkgs.python313Packages; [
        jinja2
        materialyoucolor
        pillow
      ];
    };

    home.sessionVariables = {
      # Hot reload theme in libadwaita applications
      GTK_THEME = "Material";
    };

    gtk.theme.name = "Material";
  };
}
