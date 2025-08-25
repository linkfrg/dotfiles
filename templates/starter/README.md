# A starter Home Manager config

It's a minimal starter Home Manager config which utilizies my dotfiles.

You can init it using:

```bash
nix flake init --template path:github:linkfrg/dotfiles#minimal
```

Remember to replace the placeholder parts of this flake with your own data.
For convenience, comments starting with `CHANGME:` indicate what needs to be replaced.

## Deploying

```bash
home-manager switch --flake .#username
```

If you don't have Home Manager installed, run:
```bash
nix shell nixpkgs#home-manager
```
