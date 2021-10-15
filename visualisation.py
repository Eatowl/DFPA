#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

from matplotlib.ticker import NullFormatter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import logging
import warnings
warnings.simplefilter('ignore')
matplotlib.use('TkAgg')


class Visualisation():

    def __init__(self, df):
        self.data = df
        self.roadMap = list()

    def drawFigure(self, canvas, figure):
        logging.info("Start Visualisation 'drawFigure' function")
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    def createFigure(self, data):
        logging.info("Start Visualisation 'createFigure' function")
        logging.debug("//////////////////////////////////////////")
        logging.debug("'createFigure' Data: {}".format(data.df.dtypes[1]))
        logging.debug("//////////////////////////////////////////")
        df_str = data.df.select_dtypes(include=['float64', 'float32', \
                                                'int64', 'int32', 'int16', 'int8'])
        df_str.columns
        figure = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
        figure.add_subplot(111).hist(df_str['Annual Income'], bins = 20)
        return figure

    def startVisualisation(self):
        logging.info("Start Visualisation")
        logging.debug("'startVisualisation' Data: {}".format(self.data))
        return True