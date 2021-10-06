#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-


import warnings
warnings.simplefilter('ignore')


class Visualisation():

	def __init__(self, df):
		self.data = df
		self.roadMap = list()
		self.test = [1,2,3]

	def startVisualisation(self):
		print("\nStart startVisualisation\nData: {}".format(self.data))
		return True