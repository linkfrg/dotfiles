{
  networking.firewall = {
    # make wireguard work
    checkReversePath = false;

    # make UxPlay work (launch with ``uxplay -p``)
    allowedUDPPorts = [7011 6001 6000];
    allowedTCPPorts = [7100 7000 7001];
  };
}
