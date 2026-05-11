{inputs, ...}: {
  flake.homeModules.ignis = {pkgs, ...}: {
    imports = [
      inputs.ignis.homeManagerModules.default
    ];

    home.packages = with pkgs; [
      pamixer
      inputs.ignisctl-rs.packages.${stdenv.hostPlatform.system}.ignisctl-rs
    ];

    home.file = {
      ".local/share/themes/Material".source = ../config/Material;
    };

    programs.ignis = {
      enable = true;

      addToPythonEnv = true;
      configDir = ../config/ignis;

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
