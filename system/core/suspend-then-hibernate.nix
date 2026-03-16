{
  services.logind.settings.Login = {
    HandleLidSwitch = "suspend-then-hibernate";
    HandleLidSwitchExternalPower = "suspend-then-hibernate";
  };

  systemd.sleep.settings.Sleep = {
    HibernateDelaySec = 1;
  };
}
