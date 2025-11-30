{
  inputs,
  pkgs,
  ...
}: {
  home.packages = with pkgs; [
    pamixer
    inputs.ignisctl-rs.packages.${stdenv.hostPlatform.system}.ignisctl-rs
  ];

  home.file = {
    ".local/share/themes/Material".source = ../../Material;
  };

  programs.ignis = {
    enable = true;

    addToPythonEnv = true;
    configDir = ../../ignis;

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
}
