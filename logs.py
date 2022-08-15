#!/home/denis/anaconda3/envs/env/bin/python
# -*- coding: utf-8 -*-

import logging
import functools
from logging.config import fileConfig

fileConfig('log_config.ini')
logger = logging.getLogger(__name__)
fh = logging.FileHandler('filelog.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


def syslog(func):
	@functools.wraps(func)
	def _wrapper(*args, **kwargs):
		logging.info("Start ---DECORATE--- dfpa {} function".format(func.__name__))
		if args: 
			logging.debug("DATA---DECORATE--- dfpa {} function".format(args))
		if kwargs:
			logging.debug("DATA---DECORATE--- dfpa {} function".format(kwargs))
		result = func(*args, **kwargs)
		logging.info("END ---DECORATE--- dfpa {} function".format(func.__name__))
		return result
	return _wrapper