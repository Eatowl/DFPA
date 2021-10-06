#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd
import seaborn as sns

#from source import Source

from matplotlib import pyplot as plt

import warnings
warnings.simplefilter('ignore')


class ProblemSearch():

	def __init__(self, df, roadMap):
		self.df = df
		self.roadMap = roadMap
		self.test = [1,2,3]

	def startSearch(self):
		print("\nStart startSearch")
		self.roadMap = ['Q', 'W', 'E']
		return [1,2,3], self.roadMap