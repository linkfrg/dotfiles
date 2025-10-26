{
  disko.devices = {
    disk = {
      main = {
        type = "disk";
        device = "/dev/nvme0n1";
        content = {
          type = "gpt";
          partitions = {
            ESP = {
              size = "500M";
              type = "EF00";
              content = {
                type = "filesystem";
                format = "vfat";
                mountpoint = "/boot";
                mountOptions = ["umask=0077"];
              };
            };
            luks = {
              size = "100%";
              content = {
                type = "luks";
                name = "crypted";
                extraOpenArgs = [];
                settings.allowDiscards = true;
                passwordFile = "/tmp/disk.key";
                content = {
                  type = "lvm_pv";
                  vg = "pool";
                };
              };
            };
          };
        };
      };
    };
    lvm_vg = {
      pool = {
        type = "lvm_vg";
        lvs = {
          root = {
            size = "100G";
            content = {
              type = "filesystem";
              format = "ext4";
              mountpoint = "/";
              mountOptions = ["defaults"];
            };
          };
          swap = {
            size = "12G";
            content = {
              type = "swap";
            };
          };
          data = {
            size = "100%";
            content = {
              type = "filesystem";
              format = "ext4";
              mountpoint = "/data";
              mountOptions = ["defaults"];
            };
          };
        };
      };
    };
  };
}
