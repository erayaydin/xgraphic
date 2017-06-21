import sys
import os
from shutil import *
from os import *
from subprocess import call
from pkg_resources import resource_exists, resource_filename

stubs = os.path.join(os.path.dirname(os.path.realpath(__file__)), "stubs")


def check_etc_folder():
    if not os.path.exists("/etc/xgraphic"):
        os.makedirs("/etc/xgraphic")


def resource_copy(resource, dest):
    if os.access(os.path.dirname(dest), os.W_OK):
        copy(resource_filename(__name__, 'stubs/'+resource), dest)
    else:
        print("Couldn't write to destination path:", dest)
        print("Please check your permissions.")
        sys.exit(2)


def to_nvidia():
    check_etc_folder()
    resource_copy("xorg.conf", "/etc/X11/xorg.conf")
    resource_copy("nvidia.conf", "/usr/lib/modprobe.d/nvidia.conf")
    resource_copy("60-xgraphic-nvidia.sh", "/etc/X11/xinit/xinitrc.d/60-xgraphic-nvidia.sh")

    call(["systemctl", "disable", "bumblebeed"])

    if os.path.exists("/usr/lib/modprobe.d/bumblebee.conf"):
        remove("/usr/lib/modprobe.d/bumblebee.conf")
    if os.path.exists("/etc/X11/xinit/xinitrc.d/60-xgraphic-bumblebee.sh"):
        remove("/etc/X11/xinit/xinitrc.d/60-xgraphic-bumblebee.sh")


def to_bumblebee():
    check_etc_folder()
    resource_copy("bumblebee.conf", "/usr/lib/modprobe.d/bumblebee.conf")
    resource_copy("60-xgraphic-bumblebee.sh", "/etc/X11/xinit/xinitrc.d/60-xgraphic-bumblebee.sh")
    call(["systemctl", "enable", "bumblebeed"])

    if os.path.exists("/etc/X11/xorg.conf"):
        remove("/etc/X11/xorg.conf")

    if os.path.exists("/usr/lib/modprobe.d/nvidia.conf"):
        remove("/usr/lib/modprobe.d/nvidia.conf")

    if os.path.exists("/etc/X11/xinit/xinitrc.d/60-xgraphic-nvidia.sh"):
        remove("/etc/X11/xinit/xinitrc.d/60-xgraphic-nvidia.sh")
