{
  flake.homeModules.nvim = {pkgs, ...}: {
    home.packages = [
      (import ../config/nvim {inherit pkgs;})
    ];

    home.sessionVariables."EDITOR" = "nvim";
  };
}
