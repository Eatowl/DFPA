#!/home/denis/anaconda3/bin/python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import numpy as np 
import pandas as pd

import logging
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
        self.check_memory_usage = False
        self.memory_usage_result = []

    def status_checks(self):
        logging.info("Start RoadMap 'status_checks' function")
        logging.debug("ROADMAP: Status DF:" \
               "check_of_passes - {}," \
               "emission_check - {}," \
               "check_memory_usage - {}".format(self.check_of_passes,
                                                self.emission_check,
                                                self.check_memory_usage))
        return {"check_of_passes": self.check_of_passes,
                "emission_check": self.emission_check,
                "check_memory_usage": self.check_memory_usage}


class OpenData():

    id_iter = itertools.count()

    def __init__(self, df_name : str):
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
        self.objIface = None
        self.objQuality = None

    def openData(self):
        logging.info("Start UserControl 'openData' function")
        self.df = OpenData(self.df_name)
        logging.debug(self.df.df.columns)
        logging.debug(self.df.roadMap.status_checks())
        logging.debug("openData: df_id {}".format(self.df.id))

        return self.df

    def createUserInterface(self, objUser : UserControl):
        logging.info("Start UserControl 'createUserInterface' function")
        logging.debug("Create obj createInterface." \
                        " Data file name: {}".format(self.df_name))
        self.objIface = Interface(self.df_name, objUser)
        ifaceStatus = self.objIface.printInterface()

        return ifaceStatus

    def startProblemSearch(self):
        logging.info("Start UserControl 'startProblemSearch' function")
        self.objQuality = QualityControl(self.df)
        resultSearch = self.objQuality.problemSerch()
        logging.debug("UserControl startOfDataProcessing" \
                        "result problem search: {}".format(resultSearch))

    def startProblemSolution(self):
        logging.info("Start UserControl 'startProblemSolution' function")
        
        resultSolution = self.objQuality.problemSolution(resultSearch)
        logging.debug("UserControl startOfDataProcessing" \
                        "result problem solution: {}".format(resultSolution))

    def startOfDataProcessing(self):
        logging.info("Start UserControl 'startOfDataProcessing' function")
        
        DF = self.openData()
        QC = QualityControl(DF)
        resultSearch = QC.problemSerch()
        logging.debug("UserControl startOfDataProcessing" \
                        "result problem search: {}".format(resultSearch))

        resultSolution = QC.problemSolution(resultSearch)
        logging.debug("UserControl startOfDataProcessing" \
                        "result problem solution: {}".format(resultSolution))
        
        figure = self.objIface.objVisual.createFigure(self.df)

        return [DF, QC, resultSearch, resultSolution, figure]

    def main(self, objUser):
        logging.info("Start UserControl 'main' function")
        status = self.createUserInterface(objUser)
        return True

