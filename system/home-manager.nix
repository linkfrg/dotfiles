{inputs, ...}: {
  home-manager = {
    useGlobalPkgs = true;
    useUserPackages = true;
    backupFileExtension = "backup";
    extraSpecialArgs = {inherit inputs;};
    users.link = {
      imports = [../home];
    };
  };
}
