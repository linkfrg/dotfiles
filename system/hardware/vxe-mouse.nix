{
  services.udev.extraRules = ''
    KERNEL=="hidraw*", ATTRS{idVendor}=="3554", MODE="0666"
  '';
}
