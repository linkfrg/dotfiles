{
  services.navidrome = {
    enable = true;
    environmentFile = "/run/secrets/navidrome-env";

    settings = {
      openFirewall = false; # must only run locally
      MusicFolder = "/data/linkomusic";
      DataFolder = "/data/navidrome-data";
    };
  };
}
