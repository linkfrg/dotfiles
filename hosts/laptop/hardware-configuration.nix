{lib, ...}: {
  boot.initrd.availableKernelModules = ["xhci_pci" "thunderbolt" "vmd" "ahci" "nvme" "usb_storage" "sd_mod"];
  boot.initrd.kernelModules = [];
  boot.kernelModules = ["kvm-intel"];
  boot.extraModulePackages = [];

  fileSystems."/" = {
    device = "/dev/disk/by-uuid/6efd75b2-3cef-4bab-bee4-49fa268be9d1";
    fsType = "btrfs";
    options = ["compress=zstd:3"];
  };

  fileSystems."/boot" = {
    device = "/dev/disk/by-uuid/AB4B-A755";
    fsType = "vfat";
    options = ["fmask=0022" "dmask=0022"];
  };

  nixpkgs.hostPlatform = lib.mkDefault "x86_64-linux";
}
