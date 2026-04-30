{ pkgs, ... }:
{
  programs.wireshark.enable = true;
  programs.wireshark.package = pkgs.wireshark;
  programs.wireshark.dumpcap.enable = true;
  users.users.link.extraGroups = [ "wireshark" ];
}
