{
  hardware.bluetooth.enable = true;
  services.blueman.enable = true;

  hardware.bluetooth.settings = {
    General = {
      ReconnectAttempts = 0;
    };
  };
}
