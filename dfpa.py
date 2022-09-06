#!/home/denis/anaconda3/envs/env/bin/python
# -*- coding: utf-8 -*-

import sys
import getopt
from userControl import UserControl

import logging
from logs import syslog

class Usage(Exception):

    def __init__(self, msg):
        self.msg = msg


@syslog("DFPA create obj userControl data:")
def startUserControl(data: str) -> bool:

    userControlObj = UserControl(data)
    statusUserSession = userControlObj.main(userControlObj)
    return statusUserSession

@syslog("DFPA main run userControl:")
def main(argv=None):
    logging.info("-"*80)
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
            if len(args) != 0:
                status_userControl = startUserControl(args[0])
                logging.debug('dfpa status userControl: {}'
                              .format(status_userControl))
            else:
                status_userControl = startUserControl(None)
                logging.debug('dfpa status userControl: {}'
                              .format(status_userControl))
        except getopt.error as msg:
            raise Usage(msg)
    except Usage as err:
        logging.error('dfpa error: {}'.format(err.msg))
        return 2
    logging.info("-"*80)

if __name__ == "__main__":
    sys.exit(main())
