#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-


from visualisation import Visualisation
import PySimpleGUI as sg

#from userControl import UserControl

import warnings
warnings.simplefilter('ignore')


class Interface():

	def __init__(self, df, objUser):
		self.data = df
		self.roadMap = list()
		self.objUser = objUser
		self.objVisual = Visualisation(df)
		self.test = [1,2,3]

	def getDataForVisual(self):
		if self.data is not None:
			self.objUser.df_name = self.data
			dataUserControl = self.objUser.startOfDataProcessing()
			print(dataUserControl)
		else:
			print("Data not find!")
			dataUserControl = None
		print("END")

		return dataUserControl[4]


	def printInterface(self):
		print("\nStart printInterface\nData: {}".format(self.data))

		if self.data:
			text = sg.Text(self.data)
			data = self.getDataForVisual()
		else:
			text = sg.Text(size=(15,1), key='-OUTPUT-')

		layout = [[sg.Text('Data for analysis:'), text],
					[sg.Input(key='-IN-'), sg.Button('Enter')],
					[sg.Button('Start process'), sg.Button('Exit')],
					[sg.Canvas(key='-CANVAS-')]]

		window = sg.Window('DFPA V-0.03', layout, finalize=True, 
							size=(1024, 720))

		while True:
			event, values = window.read()                  
			print('Path to data', values, event)

			if event == sg.WIN_CLOSED or event == 'Exit':
				break

			if event == 'Enter':
				window['-OUTPUT-'].update(values['-IN-'])
				self.data = values['-IN-']
				print(type(values['-IN-']))

			if event == 'Start process':
				data_figure = self.getDataForVisual()
				if data_figure:
					print("Hell yeah!")
					self.objVisual.draw_figure(
										canvas=window['-CANVAS-'].TKCanvas,
										figure=data_figure)
				print("*"*80)

		window.close()   
		return True