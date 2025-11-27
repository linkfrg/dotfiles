{
  services.navidrome = {
    enable = true;

    settings = {
      openFirewall = false; # must only run locally
      MusicFolder = "/data/linkomusic";
      DataFolder = "/data/navidrome-data";
    };
  };
}
