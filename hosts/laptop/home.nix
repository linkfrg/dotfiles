{
  imports = [
    ../common/home.nix
  ];

  custom = {
    terminal = {
      nvtop = {
        enable = true;
        intel = true;
      };
    };
  };
}
