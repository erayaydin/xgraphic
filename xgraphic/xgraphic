#!/usr/bin/python

import sys
import os
import getopt
from shutil import copyfile
from os import *
from subprocess import call

def main(argv):
    appname = path.basename(__file__)
    stubfolder = path.join(path.dirname(path.realpath(__file__)), "stubs")

    switch = 'nvidia'

    try:
        opts, args = getopt.getopt(argv, "hs:", ["switch="])
    except getopt.GetoptError:
        print(appname+' -s [nvidia,bumblebee]')
        sys.exit(2)

    for opt,arg in opts:
        if opt == '-h':
            print(appname+' -s [nvidia,bumblebee]')
            sys.exit()
        elif opt in ("-s", "--switch"):
            switch = arg

    if switch == 'nvidia':
        pass
    elif switch == 'bumblebee':
        pass
    else:
        print('You should pick nvidia or bumblebee for graphics card switch.')
        sys.exit(2)

    if os.geteuid() != 0:
        print('You should be root for switching graphic card.')
        sys.exit(2)

    if not os.path.exists("/etc/xgraphic"):
        os.makedirs("/etc/xgraphic")

    if switch == 'nvidia':
        print("Switching to nvidia card...")
        copyfile(path.join(stubfolder, "xorg.conf"), "/etc/X11/xorg.conf")
        copyfile(path.join(stubfolder, "nvidia.conf"), "/usr/lib/modprobe.d/nvidia.conf")
        copyfile(path.join(stubfolder, ".xgraphic-nvidia"), "/etc/xgraphic/.xgraphic")

        call(["systemctl", "disable", "bumblebeed"])
        remove("/usr/lib/modprobe.d/bumblebee.conf")
    else:
        print("Switching to bumblebee...")
        copyfile(path.join(stubfolder, "bumblebee.conf"), "/usr/lib/modprobe.d/bumblebee.conf")
        copyfile(path.join(stubfolder, ".xgraphic-bumblebee"), "/etc/xgraphic/.xgraphic")
        call(["systemctl", "enable", "bumblebeed"])

        remove("/etc/X11/xorg.conf")
        remove("/usr/lib/modprobe.d/nvidia.conf")

if __name__ == "__main__":
    main(sys.argv[1:])
