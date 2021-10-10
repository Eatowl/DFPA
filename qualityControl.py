#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import logging
import warnings
warnings.simplefilter('ignore')

from source import Source
from problemSolution import ProblemSolution


class QualityControl():

	def __init__(self, df):
		self.df = df
		self.roadMap = list()
		self.test = [1,2,3]

	def problemSerch(self):
		logging.info("Start QualityControl 'problemSerch' function")
		obj_source = Source(self.df)
		result = obj_source.problemSearch()
		logging.debug("'problemSerch' obj_source {}"\
										.format(obj_source.df.head()))
		self.roadMap = obj_source.roadMap
		return result

	def problemSolution(self, data):
		logging.info("Start QualityControl 'problemSolution' function")
		logging.debug("'problemSolution' data = {}".format(data))
		obj_Solution = ProblemSolution(data, self.roadMap)
		result = obj_Solution.startSolution()
		return result