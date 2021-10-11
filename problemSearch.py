#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd
import seaborn as sns

#from source import Source

from matplotlib import pyplot as plt

import logging
import warnings
warnings.simplefilter('ignore')


class ProblemSearch():

	def __init__(self, df, roadMap):
		self.df = df
		self.roadMap = roadMap
		self.test = [1,2,3]

	def searchForPasses(self):
		logging.info("Start ProblemSearch 'searchForPasses' function")
		logging.debug("*"*80)
		logging.debug(self.df.isna().sum())
		logging.debug(self.df.columns.values)
		logging.debug("*"*80)
		self.roadMap.check_of_passes = True
		for valueAndName in zip(self.df.isna().sum(), self.df.columns.values):
			if valueAndName[0] > 0:
				self.roadMap.check_of_passes_data.append(valueAndName[1])

	def startSearch(self):
		logging.info("Start ProblemSearch 'startSearch' function")
		logging.debug("ProblemSearch 'startSearch' function."\
						" Value check_of_passes: {}"\
								.format(self.roadMap.check_of_passes))
		if self.roadMap.check_of_passes is False:
			self.searchForPasses()
		logging.debug("#################################")
		logging.debug("ProblemSearch 'startSearch' function."\
						" Value check_of_passes_data: {}"\
								.format(self.roadMap.check_of_passes_data))
		logging.debug("ProblemSearch 'startSearch' function."\
						" Value check_of_passes: {}"\
								.format(self.roadMap.check_of_passes))
		logging.debug("#################################")
		
		return [1,2,3], self.roadMap