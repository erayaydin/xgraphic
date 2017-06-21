from os import *
import sys
import argparse
import xgraphic

def main():
    appname = "xgraphic"
    drivers = ["nvidia", "bumblebee"]

    parser = argparse.ArgumentParser(description='Switching graphic card.')
    parser.add_argument('driver', help='select a graphic card', choices=drivers, default='nvidia', nargs='?')
    args = parser.parse_args()

    if geteuid() != 0:
        print('You should be root for switching graphic card.')
        sys.exit(2)

    if args.driver == 'nvidia':
        print("Switching to nvidia card...")
        xgraphic.to_nvidia()
    elif args.driver == 'bumblebee':
        print("Switching to bumblebee...")
        xgraphic.to_bumblebee()

if __name__ == '__main__':
    main()
