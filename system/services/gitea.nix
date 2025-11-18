{
  services.gitea = {
    enable = true;
    user = "gitea";
    database = {
      type = "sqlite3";
    };
    httpPort = 3000;
    rootUrl = "http://localhost:3000/";
  };
}
