{
  boot.initrd.availableKernelModules = ["xhci_pci" "ahci" "usbhid" "usb_storage" "sd_mod"];
  boot.initrd.kernelModules = [];
  boot.kernelModules = ["kvm-intel"];
  boot.extraModulePackages = [];

  fileSystems."/" = {
    device = "/dev/disk/by-uuid/45da194c-26d5-4dd5-99e9-05ca2027eb47";
    fsType = "ext4";
  };

  fileSystems."/boot" = {
    device = "/dev/disk/by-uuid/C72E-A5F8";
    fsType = "vfat";
    options = ["fmask=0022" "dmask=0022"];
  };

  nixpkgs.hostPlatform = "x86_64-linux";
}
