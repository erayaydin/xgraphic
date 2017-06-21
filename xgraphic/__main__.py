from os import *
import sys
import getopt
import xgraphic

def main():
    appname = "xgraphic"
    switch = 'nvidia'

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:", ["switch="])
    except getopt.GetoptError:
        print(appname + ' -s [nvidia,bumblebee]')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(appname + ' -s [nvidia,bumblebee]')
            sys.exit()
        elif opt in ("-s", "--switch"):
            switch = arg

    if geteuid() != 0:
        print('You should be root for switching graphic card.')
        sys.exit(2)

    if switch == 'nvidia':
        print("Switching to nvidia card...")
        xgraphic.to_nvidia()
    elif switch == 'bumblebee':
        print("Switching to bumblebee...")
        xgraphic.to_bumblebee()
    else:
        print('You should pick nvidia or bumblebee for graphics card switch.')
        sys.exit(2)

if __name__ == '__main__':
    main()