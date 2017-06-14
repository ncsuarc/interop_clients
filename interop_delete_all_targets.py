from __future__ import print_function
import json
import zmq
import ARC
import math
import argparse
import sys

from ARC.interop import Interop

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-auto", "--auto", action="store_true")
    args = parser.parse_args()
    io = Interop()
    try:
        targets = io.get_targets()
        for target in targets:
            print('Deleting:')
            print(target)
            print('\n')
            if (not args.auto) and target.get('autonomous'):
                continue
            io.delete_target(target.get('id'))
    except KeyboardInterrupt:
        pass
    finally:
        pass
