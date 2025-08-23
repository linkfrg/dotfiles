{
  config,
  lib,
  ...
}: let
  cfg = config.custom.programs.virt-manager;
in {
  options.custom.programs.virt-manager = {
    enable = lib.mkEnableOption "Enable virt-manager";
  };

  config = lib.mkIf cfg.enable {
    virtualisation.libvirtd.enable = true;
    programs.virt-manager.enable = true;

    users.users.${config.custom.core.users.username}.extraGroups = [
      "libvirtd"
    ];
  };
}
