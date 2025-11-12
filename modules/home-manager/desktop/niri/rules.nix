{
  window-rules = [
    {
      geometry-corner-radius = {
        bottom-left = 15.0;
        bottom-right = 15.0;
        top-left = 15.0;
        top-right = 15.0;
      };
      clip-to-geometry = true;
    }
    {
      matches = [
        {
          app-id = "firefox$";
          title = "^Picture-in-Picture$";
        }
      ];
      open-floating = true;
    }
  ];
}
