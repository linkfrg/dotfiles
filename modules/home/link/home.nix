{self, ...}: {
  # flake.homeConfigurations.USERNAME = inputs.home-manager.lib.homeManagerConfiguration {
  #   pkgs = import inputs.nixpkgs { system = "x86_64-linux"; };
  #   modules = [
  #     self.homeModules.USERNAMEModule
  #     {
  #       home.username = "link";
  #       home.homeDirectory = "/home/link";
  #     }
  #   ];
  # };

  flake.homeModules.linkModule = {
    imports = [
      self.homeModules.niri
      self.homeModules.hyprlock
      self.homeModules.ignis
      self.homeModules.appearance
      self.homeModules.games
      self.homeModules.firefox
      self.homeModules.wlsunset
      self.homeModules.kitty
      self.homeModules.graphicalPrograms
      self.homeModules.terminalPrograms
      self.homeModules.shell
      self.homeModules.ssh
      self.homeModules.tmux
      self.homeModules.nvim
      self.homeModules.yazi
      self.homeModules.zoxide
      self.homeModules.userDirs
      self.homeModules.mimeApps
    ];

    home.username = "link";
    home.homeDirectory = "/home/link";

    home.stateVersion = "25.05";
  };
}
