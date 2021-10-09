#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
#from userControl import UserControl

import warnings
warnings.simplefilter('ignore')


class Interface():

	def __init__(self, df, objUser):
		self.data = df
		self.roadMap = list()
		self.objUser = objUser
		self.test = [1,2,3]


	def startProcess(self):
		if self.data is not None:
			self.objUser.df_name = self.data
			status = self.objUser.startProcessing()
			print(status)
		else:
			print("Data not find!")
		print("END")


	def printInterface(self):
		print("\nStart printInterface\nData: {}".format(self.data))

		if self.data:
			text = sg.Text(self.data)
			self.startProcess()
		else:
			text = sg.Text(size=(15,1), key='-OUTPUT-')

		layout = [[sg.Text('Data for analysis:'), text],
					[sg.Input(key='-IN-'), sg.Button('Enter')],
					[sg.Button('Start process'), sg.Button('Exit')]]

		window = sg.Window('DFPA V-0.03', layout, size=(1024, 720))

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
				self.startProcess()
				print("*"*80)

		window.close()   
		return True