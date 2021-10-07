#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import sys
import getopt

#from source import Source
from interface import Interface
#from userControl import UserControl

global obj_main


class Usage(Exception):

    def __init__(self, msg):
        self.msg = msg
        

def createInterface(data):
        print("\nCreate createInterface\nData and problem: {}".format(data))
        interface = Interface(data)
        status = interface.printInterface()

        return status


def main(argv = None):

    if argv is None:
        argv = sys.argv

    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
            print(args)

            if len(args) != 0:
                for arg in args:
                    print(arg)
                status_interface = createInterface(arg)
            else:
                status_interface = createInterface(None)

        except getopt.error as msg:
             raise Usage(msg)

    except Usage as err:
        print >> sys.stderr, err.msg
        print >> sys.stderr, "for help use --help"

        return 2

if __name__ == "__main__":
    sys.exit(main())