{
  inputs,
  pkgs,
  ...
}: let
  firefox-addons = inputs.firefox-addons.packages.${pkgs.stdenv.hostPlatform.system};
in {
  xdg.mimeApps = {
    enable = true;
    defaultApplications = {
      "default-web-browser" = ["firefox.desktop"];
      "text/html" = ["firefox.desktop"];
      "x-scheme-handler/http" = ["firefox.desktop"];
      "x-scheme-handler/https" = ["firefox.desktop"];
      "x-scheme-handler/about" = ["firefox.desktop"];
      "x-scheme-handler/unknown" = ["firefox.desktop"];
      "application/pdf" = ["firefox.desktop"];
    };
  };

  programs.firefox = {
    enable = true;

    # Check about:policies#documentation for options
    policies = import ./policies.nix;

    profiles.default = {
      id = 0;
      name = "default";
      isDefault = true;

      extensions.packages = import ./extensions.nix {inherit firefox-addons;};
      settings = import ./settings.nix;
    };
  };
}
