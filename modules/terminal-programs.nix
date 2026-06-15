{
  flake.nixosModules.terminalPrograms = {pkgs, ...}: {
    environment.systemPackages = with pkgs; [
      usbutils
      libva-utils
      tree
      vim
    ];

    programs.fish.enable = true;

    documentation.man.cache.enable = false; # speed up building

    environment.variables."EDITOR" = "vim";
  };

  flake.homeModules.shell = {
    programs.fish = {
      enable = true;
      interactiveShellInit = ''
        set -g fish_greeting
        set --global fish_color_command blue
      '';
    };

    programs.starship = {
      enable = true;
      enableFishIntegration = true;
      settings = {
        add_newline = false;
        format = builtins.concatStringsSep "" [
          "$os"
          "$directory"
          "$git_branch"
          "$git_status"
          "$fill"
          "$python"
          "\n$character"
        ];
        character = {
          success_symbol = "[❯](bold green)";
          error_symbol = "[✗](bold red)";
        };

        fill = {
          symbol = " ";
        };
      };
    };
  };

  flake.homeModules.terminalPrograms = {pkgs, ...}: {
    programs.btop.enable = true;

    programs.direnv = {
      enable = true;
      # enableFishIntegration = true;
      nix-direnv.enable = true;
      silent = true;
    };

    programs.git = {
      enable = true;

      settings = {
        user = {
          name = "Link";
          email = "linkfrg.dev@proton.me";
        };

        init.defaultBranch = "main";
      };
    };

    programs.fastfetch = {
      enable = true;

      settings = {
        logo = {
          type = "small";
        };

        general = {
          detectVersion = false;
        };

        modules = [
          "title"
          {
            type = "os";
            format = "{name}";
          }
          "packages"
          "shell"
          {
            type = "wm";
            format = "{pretty-name}";
          }
          "terminal"
          "memory"
        ];
      };
    };

    programs.man.generateCaches = false; # speed up building
    home.packages = with pkgs; [
      cmatrix
      cava
      gh
      speedtest-cli
      cloc
      act
      wl-clipboard
      lazygit
    ];
  };
}
