#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

from visualisation import Visualisation
import PySimpleGUI as sg

import logging
import warnings
warnings.simplefilter('ignore')


class Interface():

	def __init__(self, df, objUser):
		self.data = df
		self.roadMap = list()
		self.objUser = objUser
		self.objVisual = Visualisation(df)

	def getDataForVisual(self):
		logging.info("Start Interface 'getDataForVisual' function")
		if self.data is not None:
			self.objUser.df_name = self.data
			dataUserControl = self.objUser.startOfDataProcessing()
			logging.debug("dataUserControl: {}".format(dataUserControl))
		else:
			logging.warnings("'getDataForVisual' Data not find!")
			dataUserControl = None

		return dataUserControl[4]


	def printInterface(self):
		logging.info("Start Interface 'printInterface' function")

		if self.data:
			logging.debug("Check data in Interface." \
							" Data file name: {}".format(self.data))
			text = sg.Text(self.data)
			data = self.getDataForVisual()
		else:
			logging.debug("Check data in Interface. Data file name: Empty")
			text = sg.Text(size=(15,1), key='-OUTPUT-')

		layout = [[sg.Text('Data for analysis:'), text],
				  [sg.Input(key='-IN-'), sg.Button('Enter')],
				  [sg.Button('Start process'), sg.Button('Exit')],
				  [sg.Canvas(key='-CANVAS-')]]

		window = sg.Window('DFPA V-0.04', layout, finalize=True, 
							size=(1024, 720))

		while True:
			event, values = window.read()
			logging.debug("Output window.read:" \
							" event = {} values = {}".format(event, values))               

			if event == sg.WIN_CLOSED or event == 'Exit':
				logging.debug("Quit dfpa")
				break

			if event == 'Enter':
				logging.debug("Input data in interface: {}" \
													.format(values['-IN-']))
				window['-OUTPUT-'].update(values['-IN-'])
				self.data = values['-IN-']

			if event == 'Start process':
				logging.debug("Start process, run getDataForVisual")
				data_figure = self.getDataForVisual()
				if data_figure:
					logging.debug("Print graph in window")
					self.objVisual.drawFigure(canvas=window['-CANVAS-'].TKCanvas,
											   figure=data_figure)

		window.close()   
		return True