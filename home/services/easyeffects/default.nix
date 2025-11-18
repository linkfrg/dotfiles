let
  loadPreset = path: builtins.fromJSON (builtins.readFile path);
in {
  services.easyeffects = {
    enable = true;
    preset = "main";
    extraPresets = {
      main = loadPreset ./output/main.json;
    };
  };
}
