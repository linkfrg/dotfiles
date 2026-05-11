{inputs, ...}: {
  imports = [
    inputs.home-manager.flakeModules.home-manager
  ];

  systems = ["x86_64-linux"];
}
