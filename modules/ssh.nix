{
  flake.homeModules.ssh = {
    programs.ssh = {
      enable = true;
      enableDefaultConfig = false;

      matchBlocks = {
        "github.com" = {
          identityFile = "/run/secrets/ssh/github/private";
        };
      };
    };
  };
}
