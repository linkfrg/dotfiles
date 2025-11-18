{
  services.avahi = {
    enable = true;
    nssmdns4 = true;

    publish = {
      enable = true;
      userServices = true;
      addresses = true;
    };
  };
}
