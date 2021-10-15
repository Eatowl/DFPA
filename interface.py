#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

from screeninfo import get_monitors
from visualisation import Visualisation
import PySimpleGUI as sg

import logging
import warnings
warnings.simplefilter('ignore')


class Interface():

    def __init__(self, df, objUser):
        self.data_name = df
        self.objUser = objUser
        self.objVisual = Visualisation(df)

    def getWindowSize(self):
        logging.info("Start Interface 'getWindowSize' function")
        screen = get_monitors()
        screen2 = get_monitors()[1]
        logging.debug("len(screen) {}".format(len(screen)))
        logging.debug("screen2 {}".format(screen2))
        #width, hight = screen[0][0]
        return screen[0].width, screen[0].height

    def updateTextField(self, window, data):
        logging.info("Start Interface 'updateTextField' function")
        text_elem = window['-text-']
        text_elem.update("Verification data:\n-data with gaps:\n {}".format(data))

    def getDataForVisual(self):
        logging.info("Start Interface 'getDataForVisual' function")
        if self.data_name is not None:
            self.objUser.df_name = self.data_name
            dataUserControl = self.objUser.startOfDataProcessing()
            logging.debug("dataUserControl: {}".format(dataUserControl))
        else:
            logging.warnings("'getDataForVisual' Data not find!")
            dataUserControl = None

        return dataUserControl[4]

    def printInterface(self):
        logging.info("Start Interface 'printInterface' function")

        if self.data_name:
            logging.debug("Check data in Interface." \
                            " Data file name: {}".format(self.data_name))
            text = sg.Text(self.data_name)
            #data = self.getDataForVisual()
        else:
            logging.debug("Check data in Interface. Data file name: Empty")
            text = sg.Text(size=(45,1), key='-OUTPUT-')

        layout = [[sg.Text('Data for analysis:'), text],
                  [sg.Text('Data for analysis: ', size=(15, 1)), sg.InputText(),\
                   sg.FileBrowse(file_types=(("csv files", "*.csv"),)),\
                   sg.Button('Open')],
                  [sg.Button('Data integrity check'),\
                   sg.Button('Error correction'),\
                   sg.Button('Visualisation'),\
                   sg.Button('Exit')],
                  [sg.Canvas(key='-CANVAS-'),\
                   sg.Text('verification data:', size=(900, 10), key='-text-')]]

        width, height = self.getWindowSize()
        height = height - 40
        window = sg.Window('DFPA V-0.0.4', layout, finalize=True,
                                           size=(width-150, height-150))

        while True:
            event, values = window.read()
            logging.debug("Output window.read:" \
                            " event = {} values = {}".format(event, values))

            if event == sg.WIN_CLOSED or event == 'Exit':
                logging.debug("Quit dfpa")
                break

            if event == 'Open':
                logging.debug("Input data in interface: {}" \
                                                    .format(values['Browse']))
                window['-OUTPUT-'].update(values['Browse'])
                self.data_name = values['Browse']

            if event == 'Data integrity check':
                logging.debug("Start process, run getDataForVisual")
                logging.debug("Print data in objUser {}"\
                       .format(self.objUser.df.roadMap.check_of_passes_data))
                self.updateTextField(window,\
                                 self.objUser.df.roadMap.check_of_passes_data)

            if event == 'Error correction':
                logging.debug("Start process, run getDataForVisual")
                logging.debug("Print data in objUser {}"\
                            .format(self.objUser.df.roadMap.emission_check))
                self.updateTextField(window,\
                                 self.objUser.df.roadMap.emission_check)

            if event == 'Visualisation':
                logging.debug("Start process, run getDataForVisual")
                data_figure = self.getDataForVisual()
                if data_figure:
                    logging.debug("Print graph in window")
                    logging.debug("Print data in objUser {}"\
                        .format(self.objUser.df.roadMap.check_of_passes_data))
                    self.objVisual.drawFigure(canvas=window['-CANVAS-'].TKCanvas,
                                               figure=data_figure)

        window.close()
        return True