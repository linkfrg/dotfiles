{pkgs, ...}: {
  home.packages = with pkgs; [
    nil
  ];
  programs.zed-editor = {
    enable = true;

    extraPackages = with pkgs; [
      nil
      alejandra
      rust-analyzer
    ];

    extensions = import ./extensions.nix;
    themes = import ./themes.nix;
    userSettings = import ./settings.nix;
    userKeymaps = import ./keymaps.nix;
  };
}
