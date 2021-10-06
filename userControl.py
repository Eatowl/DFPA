#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd

import itertools

#from interface import Interface
from visualisation import Visualisation
from qualityControl import QualityControl


import warnings
warnings.simplefilter('ignore')



class RoadMap():

	def __init__(self, df_id, data):
		self.df_id = df_id
		self.data = data
		self.check_of_passes = False
		self.check_of_passes_data = []
		self.emission_check = False
		self.emission_check_data = []

	def status_checks(self):
		print("ROADMAP: Status DF:\
			   check_of_passes - {},\
			   emission_check - {}".format(self.check_of_passes,
			   							   self.emission_check ))
		return {"check_of_passes": self.check_of_passes,
				"emission_check": self.emission_check}



class OpenData():

	id_iter = itertools.count()

	def __init__(self, df):
		self.id = next(self.id_iter)
		self.df = pd.read_csv(df)
		self.roadMap = RoadMap(self.id, self.df)

	def __len__(self):
		return len(self.df)

	def get_id(self):
		return self.id



class UserControl():

	def __init__(self, df):
		self.df = df
		self.test = [1,2,3]

	'''def createInterface(self, data):
		print("\nCreate createInterface\nData and problem: {}".format(data))
		interface = Interface(data)
		status = interface.printInterface()
		return status'''

	def newVisualisation(self, data):
		print("\nCreate newVisualisation\nData: {}".format(data))
		visual = Visualisation(data)
		status = visual.startVisualisation()
		return status

	'''def openData(self, data):
		print("\nOpen and save data \n")
		interface = Interface(data)
		status = interface.printInterface()
		return data'''

	def startProcessing(self):
		print("Start startProcessing")
		'''if self.df is not None:
			DF = OpenData(self.df)
		else:
			status_interface = self.createInterface("None")'''
		DF = OpenData(self.df)

		print(DF.roadMap.status_checks())
		print(DF.id)
		print("=====")
		print(self.df)

		QC = QualityControl(DF)
		resultSearch = QC.problemSerch()
		print("Output data: {}".format(resultSearch))

		#status_interface = self.createInterface(resultSearch)

		resultSolution = QC.problemSolution(resultSearch)
		print("\nSolution data: {}".format(resultSolution))

		status_visualisation = self.newVisualisation(resultSolution)
		return [DF, QC, resultSearch, resultSolution, status_visualisation]

