{pkgs, ...}: {
  # One of the usb ports is dead and kernel stucks in a loop trying to power-manage it
  # leading to kworker loading CPU up to 10% overall and 100% on one core
  # So, this disables Power Management on usb3
  #
  # To debug use btop and
  # $ sudo -s
  # $ echo l > /proc/sysrq-trigger
  # $ dmesg -w
  services.udev.extraRules = ''
    ACTION=="add", SUBSYSTEM=="usb", KERNEL=="usb3", ATTR{power/control}="on"
  '';

  # hack to make suspend working
  powerManagement = {
    enable = true;

    powerDownCommands = ''
      ${pkgs.kmod}/bin/modprobe -r xhci_pci
    '';

    resumeCommands = ''
      ${pkgs.kmod}/bin/modprobe xhci_pci
    '';
  };
}
