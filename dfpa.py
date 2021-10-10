#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import sys
import getopt
from userControl import UserControl

import logging
from logging.config import fileConfig

import userControl, interface, visualisation
import qualityControl, problemSearch, problemSolution

fileConfig('log_config.ini')
logger = logging.getLogger()
fh = logging.FileHandler('filelog.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


class Usage(Exception):

    def __init__(self, msg):
        self.msg = msg
    
        
def startUserControl(data):
    logger.info("Start dfpa 'startUserControl' function")
    logger.debug("Create obj UserControl. Data file name: {}".format(data))
    userControlObj = UserControl(data)
    statusUserSession = userControlObj.main(userControlObj)

    return statusUserSession

def main(argv = None):
    logger.info("||||||||||||||||||||||||||||||||||||||")
    logger.info("Start dfpa 'main' function")
    logger.info("||||||||||||||||||||||||||||||||||||||")

    if argv is None:
        argv = sys.argv

    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])

            if len(args) != 0:
                logger.debug('dfpa main run userControl data: {}'.format(args[0]))
                status_userControl = startUserControl(args[0])
            else:
                logger.debug('dfpa main run userControl data: Empty')
                status_userControl = startUserControl(None)

        except getopt.error as msg:
             raise Usage(msg)

    except Usage as err:
        print >> sys.stderr, err.msg
        print >> sys.stderr, "for help use --help"

        return 2

if __name__ == "__main__":
    sys.exit(main())