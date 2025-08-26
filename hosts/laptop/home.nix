{
  inputs,
  outputs,
  ...
}: {
  imports = [
    outputs.homeManagerModules.default
    outputs.homeManagerModules.public
    inputs.dotfiles-private.homeManagerModules.default
  ];

  custom = {
    bundles.general-desktop.enable = true;

    terminal = {
      nvtop = {
        enable = true;
        intel = true;
      };
    };
  };
}
