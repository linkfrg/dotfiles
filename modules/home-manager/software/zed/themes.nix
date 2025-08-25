let
  themeFile = builtins.fetchurl {
    url = "https://github.com/catppuccin/zed/releases/download/v0.2.23/catppuccin-blue.json";
    sha256 = "7b160dbece4d845a642d642369cb0b7119f591d258df7d3fc479a43bb18018af";
  };

  themeJson = builtins.fromJSON (builtins.readFile themeFile);
in {
  # For some reason passing "themeFile" directly (as path) makes theme not available in Zed
  "catppuccin-blue" = themeJson;
}
