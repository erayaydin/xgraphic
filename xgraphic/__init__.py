#!/usr/bin/python

import os
from shutil import *
from os import *
from subprocess import call

stubs = os.path.join(os.path.dirname(os.path.realpath(__file__)), "stubs")

def check_etc_folder():
    if not os.path.exists("/etc/xgraphic"):
        os.makedirs("/etc/xgraphic")

def to_nvidia():
    check_etc_folder()
    copy(stubs+"/xorg.conf", "/etc/X11/xorg.conf")
    copy(stubs+"/nvidia.conf", "/usr/lib/modprobe.d/nvidia.conf")
    copy(stubs+"/60-xgraphic-nvidia.sh", "/etc/X11/xinit/xinitrc.d/60-xgraphic-nvidia.sh")

    call(["systemctl", "disable", "bumblebeed"])
    if os.path.exists("/usr/lib/modprobe.d/bumblebee.conf"):
        remove("/usr/lib/modprobe.d/bumblebee.conf")
    if os.path.exists("/etc/X11/xinit/xinitrc.d/60-xgraphic-bumblebee.sh"):
        remove("/etc/X11/xinit/xinitrc.d/60-xgraphic-bumblebee.sh")

def to_bumblebee():
    check_etc_folder()
    copy(stubs+"/bumblebee.conf", "/usr/lib/modprobe.d/bumblebee.conf")
    copy(stubs+"/60-xgraphic-bumblebee.sh", "/etc/X11/xinit/xinitrc.d/60-xgraphic-bumblebee.sh")
    call(["systemctl", "enable", "bumblebeed"])

    if os.path.exists("/etc/X11/xorg.conf"):
        remove("/etc/X11/xorg.conf")

    if os.path.exists("/usr/lib/modprobe.d/nvidia.conf"):
        remove("/usr/lib/modprobe.d/nvidia.conf")

    if os.path.exists("/etc/X11/xinit/xinitrc.d/60-xgraphic-nvidia.sh"):
        remove("/etc/X11/xinit/xinitrc.d/60-xgraphic-nvidia.sh")