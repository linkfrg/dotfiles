{pkgs}: let
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
  pkgs.wrapNeovimUnstable pkgs.neovim-unwrapped {
    withPython3 = true;
    wrapRc = false;
    wrapperArgs = pkgs.lib.strings.concatStringsSep " " [
      ''--suffix PATH : "${pkgs.lib.makeBinPath bins}"''
    ];
  }
