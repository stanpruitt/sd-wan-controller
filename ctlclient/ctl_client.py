import sys, getopt
import ctlclient.tunnel

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "d", ["region=", "thinedge=", "fatedge=", "detail", "edgename="])
    except getopt.GetoptError:
        print("python ctl_client.py [options] commands ...")
        print("for example: python ctl_client.py --detail  --name tun13 --edge fat --thinedge thin region baicells tunnel create")
        sys.exit(2)

    if args[0] == "tunnel":
        ctlclient.tunnel.Tunnel().command(args[1:], opts)
