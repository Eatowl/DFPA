#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt

from problemSearch import ProblemSearch


import warnings
warnings.simplefilter('ignore')


class Source():

	def __init__(self, df):
		self.df = df.df
		self.roadMap = df.roadMap
		self.test = [1,2,3]

	def __len__(self):
		return len(self.df)

	def problemSearch(self):
		problemData = ProblemSearch(self.df, self.roadMap)
		result, self.roadMap = problemData.startSearch()
		return result