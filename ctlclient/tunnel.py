import http.client, urllib.parse
import subprocess
import ctlclient.util

class Tunnel():
    def command(self, args, opts):
        if args[0] == "create":
            ctlclient.util.Util().http_post("/tunnel/create", ctlclient.util.Util().opts_to_params(opts))






