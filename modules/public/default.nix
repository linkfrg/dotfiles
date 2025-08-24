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
    ./xdg-portal.nix
  ];
}
