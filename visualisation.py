#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

from matplotlib.ticker import NullFormatter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import warnings
warnings.simplefilter('ignore')

matplotlib.use('TkAgg')


class Visualisation():

	def __init__(self, df):
		self.data = df
		self.roadMap = list()
		self.test = [1,2,3]

	def draw_figure(self, canvas, figure):
		figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
		figure_canvas_agg.draw()
		figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
		return figure_canvas_agg

	def create_figure(self, data):
		figure = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
		t = np.arange(0, 3, .01)
		figure.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
		return figure

	def startVisualisation(self):
		print("\nStart startVisualisation\nData: {}".format(self.data))
		return True