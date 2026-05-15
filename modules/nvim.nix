{self, ...}: {
  perSystem =
    { pkgs, lib, ... }:
    let
      bins = with pkgs; [
        ripgrep
        fd
        fzf
        gcc
        unzip
        luajitPackages.luarocks
        pyright
        gnumake
        stylua
        lua-language-server
        tree-sitter
        rust-analyzer
        ruff
        nil
      ];
    in
    {
      packages.mynvim = pkgs.wrapNeovimUnstable pkgs.neovim-unwrapped {
        withPython3 = true;
        wrapRc = false;
        wrapperArgs = lib.strings.concatStringsSep " " [
          ''--suffix PATH : "${lib.makeBinPath bins}"''
        ];
      };
    };

  flake.homeModules.nvim =
    { pkgs, ... }:
    {
      home.packages = [
        self.packages.${pkgs.system}.mynvim
      ];

      home.sessionVariables."EDITOR" = "nvim";
    };

}
