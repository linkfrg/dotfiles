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
    ./wayland-env.nix
    ./xdg-portal.nix
  ];
}
