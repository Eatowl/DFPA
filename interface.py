#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
from tkinter import * 
from userControl import UserControl
from sys import platform

import warnings
warnings.simplefilter('ignore')


class Interface():

	def __init__(self, df):
		self.data = df
		self.roadMap = list()
		self.test = [1,2,3]


	def getResolution(self, window):

		window.update_idletasks()
		screen_width = window.winfo_screenwidth()
		screen_height = window.winfo_screenheight()

		# определение разрешения при помощи сторонних источников линукса и винды

		#t.update()
		window.attributes('-zoomed', True)
		#window.state('zoomed')
		m_1_height= window.winfo_height()
		m_1_width= window.winfo_width()


		print(m_1_width, m_1_height)
		print("*"*80)
		print(screen_width, screen_height)


		screen_resolution = str(screen_width)+'x'+str(screen_height)

		return screen_resolution


	def checkGeometry(self):
		if platform == "linux" or platform == "linux2":
    		# linux
			print("LINUX")
		elif platform == "darwin":
    		# OS X
			print("OSX")
		elif platform == "win32":
			print("WINDOWS")
		

	def createInterface(self):
		window = Tk()
		#screen_resolution = self.getResolution(window)
		window.title("DFPA V-0.02")
		window.geometry('640x420')
		return window

	def startProcess(self):
		if self.data is not None:
			clear_data = UserControl(self.data)
			status = clear_data.startProcessing()
			print(status)
		else:
			print("Data not find!")
		print("END")


	def clicked(self, txt, lbl):

		self.data = txt.get()
		lbl.configure(text=self.data)


	def printDataCheck(self, window):

		lbl = Label(window, text="Данные для анализа: {}".format(self.data),
														font=("Arial Bold", 10))  
		lbl.grid(column=0, row=0)


	def printInterface(self):
		print("\nStart printInterface\nData: {}".format(self.data))

		if self.data:
			text = sg.Text(self.data)
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