{inputs, ...}: {
  flake.nixosModules.niri = {pkgs, ...}: {
    imports = [
      inputs.niri-flake.nixosModules.niri
    ];

    systemd.user.services.niri-flake-polkit.enable = false;

    programs.niri = {
      enable = true;
      package = pkgs.niri;
    };
  };
}
