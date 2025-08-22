{
  config,
  lib,
  ...
}: let
  cfg = config.linkfrg-dotfiles.programs.virt-manager;
in {
  options.linkfrg-dotfiles.programs.virt-manager = {
    enable = lib.mkEnableOption "Enable virt-manager";
  };

  config = lib.mkIf cfg.enable {
    virtualisation.libvirtd.enable = true;
    programs.virt-manager.enable = true;

    users.users.link.extraGroups = [
      "libvirtd"
    ];
  };
}
