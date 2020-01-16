# !/usr/bin/python3
# Description: install sd-wan edgepoll service
# By vewe-richard@github, 2020/01/10
#

import sys
import os
import subprocess
import getpass

def runningUnderGitProjectRootDirectory(cwd):
    return os.path.isdir(os.path.join(cwd, "controllerv2"))

if __name__ == "__main__":
    assert sys.version_info >= (3, 0)
    assert runningUnderGitProjectRootDirectory(os.getcwd())
    #check if systemd is support
    assert os.path.isdir("/lib/systemd/system/")
    with open("./controllerv2/controllerv2.service") as f:
        tmp = f.read().replace("{GITROOT}", os.getcwd())
        serviceFile = tmp.replace("{user}", getpass.getuser())
    #write to /lib/systemd/system
    with open("/lib/systemd/system/controllerv2.service", "w") as f:
        f.write(serviceFile)
    subprocess.run(["systemctl", "disable", "controllerv2.service"])
    subprocess.run(["systemctl", "stop", "controllerv2.service"])
    subprocess.run(["systemctl", "daemon-reload"])
    subprocess.run(["systemctl", "start", "controllerv2.service"])
    subprocess.run(["systemctl", "enable", "controllerv2.service"])
    print("Install Complete")
    print("Please run 'systemctl status controllerv2' to check service status")
