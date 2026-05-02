{ pkgs, ... }:
{
  imports = [
    ./kitty.nix
    ./firefox.nix
  ];

  programs.mpv = {
    enable = true;
    config = {
      audio-file-auto = "fuzzy";
    };
  };

  home.packages = with pkgs; [
    telegram-desktop
    ayugram-desktop
    vesktop
    proton-vpn
    eog
    transmission_4-gtk
    xeyes
    uxplay
    pinta
    gnome-calculator
    linux-wifi-hotspot
    snapshot
    pavucontrol
    obsidian
    ferdium
    gapless
    super-productivity
    libreoffice
    (import ./neovim.nix {
      inherit pkgs;
    })
  ];

}
