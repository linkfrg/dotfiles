{
  self,
  inputs,
  ...
}: {
  imports = [
    ./hyprland
    ./hyprlock
    (import ./ignis.nix {inherit self inputs;})
    ./kitty.nix
    ./cursor-theme.nix
    ./fonts.nix
    ./icon-theme.nix
  ];
}
