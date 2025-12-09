{pkgs, ...}: {
  systemd.user.services.niri-flake-polkit.enable = false;

  programs.niri = {
    enable = true;
    package = pkgs.niri;
  };
}
