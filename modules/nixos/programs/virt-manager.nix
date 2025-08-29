{
  config,
  lib,
  pkgs,
  ...
}: let
  cfg = config.custom.programs.virt-manager;
in {
  options.custom.programs.virt-manager = {
    enable = lib.mkEnableOption "Enable virt-manager";
  };

  config = lib.mkIf cfg.enable {
    virtualisation.libvirtd = {
      enable = true;
      qemu.vhostUserPackages = with pkgs; [virtiofsd];
    };
    programs.virt-manager.enable = true;
  };
}
