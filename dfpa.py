#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import sys
import getopt

#from source import Source
#from interface import Interface
from userControl import UserControl



class Usage(Exception):

    def __init__(self, msg):
        self.msg = msg
        

def startUserControl(data):
    print("\nCreate obj UserControl\nData and problem: {}".format(data))
    userControlObj = UserControl(data)
    statusUserSession = userControlObj.main(userControlObj)

    return statusUserSession


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
                #status_interface = createInterface(arg)
                status_userControl = startUserControl(arg)
            else:
                #status_interface = createInterface(None)
                status_userControl = startUserControl(None)

        except getopt.error as msg:
             raise Usage(msg)

    except Usage as err:
        print >> sys.stderr, err.msg
        print >> sys.stderr, "for help use --help"

        return 2

if __name__ == "__main__":
    sys.exit(main())