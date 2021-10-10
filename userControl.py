#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import numpy as np 
import pandas as pd

import itertools

from interface import Interface
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

	def __init__(self, df_name):
		self.id = next(self.id_iter)
		self.df = pd.read_csv(df_name)
		self.roadMap = RoadMap(self.id, self.df)

	def __len__(self):
		return len(self.df)

	def get_id(self):
		return self.id


class UserControl():

	def __init__(self, df):
		self.df_name = df
		self.df = None
		self.iface = None
		self.test = [1,2,3]

	'''def newVisualisation(self, data):
		print("\nCreate newVisualisation\nData: {}".format(data))
		visual = Visualisation(data)
		status = visual.startVisualisation()

		return status'''

	def openData(self):
		print("\nOpen and save data \n")
		DF = OpenData(self.df_name)
		print(DF.roadMap.status_checks())
		print(DF.id)
		print("=====")
		print(self.df_name)

		return DF

	def createUserInterface(self, objUser):
		print("\nCreate createInterface\nData and problem: {}".format(self.df_name))
		self.iface = Interface(self.df_name, objUser)
		ifaceStatus = self.iface.printInterface()

		return ifaceStatus

	def startOfDataProcessing(self):
		print("Start startProcessing")
		
		DF = self.openData()
		QC = QualityControl(DF)
		resultSearch = QC.problemSerch()
		print("Output data: {}".format(resultSearch))
		resultSolution = QC.problemSolution(resultSearch)
		print("\nSolution data: {}".format(resultSolution))
		figure = self.iface.objVisual.create_figure("DATA")

		return [DF, QC, resultSearch, resultSolution, figure]

	def main(self, objUser):
		print("Start main UserControl")
		status = self.createUserInterface(objUser)

		return True

