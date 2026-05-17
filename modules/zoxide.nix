{
  flake.homeModules.zoxide = {
    programs.zoxide = {
      enable = true;
      enableFishIntegration = true;
    };

    programs.fish.shellAliases = {
      cd = "z";
    };
  };
}
