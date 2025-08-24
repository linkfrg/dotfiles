# Installation

> [!IMPORTANT]
> The knowledge of Nix & NixOS is required.

## Using Home Manager modules

> [!TIP]
> You can start with the [starter flake template](https://github.com/linkfrg/dotfiles/blob/main/templates/starter).

Since this is my personal, hardware-specific configuration, many parts may be inappropriate for your use case.
However, you can reuse some of my configs in your own setup. This flake exports a public Home Manager module, which includes Ignis, Hyprland and hyprlock.

1. Add this repo to your flake's inputs:

```nix
{
  inputs = {
    linkfrg-dotfiles = {
      url = "github:linkfrg/dotfiles";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };
}
```

2. Add the Home Manager module:

```nix
# home.nix
{inputs, ...}: {
  imports = [
    inputs.linkfrg-dotfiles.homeManagerModules.public
  ];
}
```

3. Enable modules you want

```nix
# home.nix
{
  linkfrg-dotfiles = {
    hyprland.enable = true;
    hyprlock.enable = true;
    ignis.enable = true;
    kitty.enable = true;
  };
}
```

For the list of all available options, see [modules](https://github.com/linkfrg/dotfiles/tree/main/modules/public).

### Running on non-NixOS distro

> [!DANGER]
> Not tested, not recommended. You're on your own here.

It's still possible to use Home Manager on distros rather than NixOS, though running graphical applications may be tricker.

You have to install the [Nix package manager](https://nixos.org/download) and run graphical apps (such as Hyprland, Ignis, Hyprland, kitty, etc.) using [NixGL](https://github.com/nix-community/nixGL).
