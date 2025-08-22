[
  {
    context = "Terminal";
    bindings = {
      # Directly pass these keys to terminal apps instead of having Zed handle them.
      ctrl-o = [
        "terminal::SendKeystroke"
        "ctrl-o"
      ];
      ctrl-s = [
        "terminal::SendKeystroke"
        "ctrl-s"
      ];
      ctrl-q = [
        "terminal::SendKeystroke"
        "ctrl-q"
      ];
    };
  }
]
