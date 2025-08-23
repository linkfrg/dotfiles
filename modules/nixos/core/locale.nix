{
  config,
  lib,
  ...
}: let
  cfg = config.custom.core.locale;
in {
  options.custom.core.locale = {
    enable = lib.mkEnableOption "Enable locale settings";
  };

  config = lib.mkIf cfg.enable {
    time.timeZone = "Asia/Almaty";
    i18n.defaultLocale = "en_US.UTF-8";

    i18n.extraLocaleSettings = {
      LC_ADDRESS = "en_US.UTF-8";
      LC_IDENTIFICATION = "en_US.UTF-8";
      LC_MEASUREMENT = "en_US.UTF-8";
      LC_MONETARY = "en_US.UTF-8";
      LC_NAME = "en_US.UTF-8";
      LC_NUMERIC = "en_US.UTF-8";
      LC_PAPER = "en_US.UTF-8";
      LC_TELEPHONE = "en_US.UTF-8";
      LC_TIME = "en_US.UTF-8";
    };
  };
}
