{inputs, ...}: {
  home-manager = {
    useGlobalPkgs = true;
    useUserPackages = true;
    backupFileExtension = "backup";
    extraSpecialArgs = {inherit inputs;};
    users.link = {
      xdg.configFile."mimeapps.list".force = true;
      imports = [../home];
    };
  };
}
