{
  flake.nixosModules.steam = {pkgs, ...}: {
    programs.steam = {
      enable = true;
      extraCompatPackages = [pkgs.proton-ge-bin];
    };

    programs.gamemode.enable = true;
  };
  flake.homeModules.games = {pkgs, ...}: {
    home.packages = with pkgs; [
      prismlauncher
      osu-lazer-bin
    ];
  };
}
