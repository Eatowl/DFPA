#!/home/denis/anaconda3/envs/env/bin/python
# -*- coding: utf-8 -*-

import logging
import functools
from logging.config import fileConfig


def syslog(log_message):
    def decorate(func):
        fileConfig('log_config.ini')

        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            logging.info("Start dfpa {} function".format(func.__name__))
            if args:
                logging.debug("{} - {}".format(log_message, args))
            if kwargs:
                logging.debug("{} - {}".format(log_message, kwargs))
            result = func(*args, **kwargs)
            logging.info("END dfpa {} function".format(func.__name__))
            return result

        return _wrapper
    return decorate
