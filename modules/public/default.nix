{
  self,
  inputs,
  ...
}: {
  imports = [
    ./hyprland
    ./hyprlock
    (import ./ignis.nix {inherit self inputs;})
    ./wayland-env.nix
    ./xdg-portal.nix
  ];
}
