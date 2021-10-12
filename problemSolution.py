#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt

import logging
import warnings
warnings.simplefilter('ignore')


class ProblemSolution():

	def __init__(self, df, roadMap):
		self.df = df
		self.roadMap = roadMap

	def startSolution(self):
		logging.info("Start ProblemSolution 'startSolution' function")
		logging.debug("'startSolution' Data = {}".format(self.df))
		logging.debug("'startSolution' RoadMap = {}".format(self.roadMap))
		return [4, 5, 6]