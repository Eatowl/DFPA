from __future__ import annotations

import numpy as np 
import pandas as pd

import logging
import itertools

from sklearn.model_selection import train_test_split

from interface import Interface
from visualisation import Visualisation
from qualityControl import QualityControl
from logs import syslog

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


class WorkingData():

    id_iter = itertools.count()

    def __init__(self, df_name : str):
        self.id = next(self.id_iter)
        self.df = pd.read_csv(df_name)
        self.roadMap = RoadMap(self.id, self.df)
        self.train_set = None
        self.test_set = None

    def __len__(self):
        return len(self.df)

    def get_id(self):
        return self.id

    def createTrainAndTestSet(self):  #Fix name function
        logging.info("Start WorkingData 'createTrainAndTestSet' function")
        
        self.train_set, self.test_set = train_test_split(self.df, \
                                                         test_size=0.2, \
                                                         random_state=42)
        logging.debug("WorkingData startOfDataProcessing" \
                        "Test_set.head(): {}".format(self.test_set.head()))


class UserControl():

    def __init__(self, file_name):
        self.df_name = file_name
        self.objData = None
        self.objIface = None
        self.objQuality = None

    def openData(self):
        logging.info("Start UserControl 'openData' function")
        if self.df_name is not None:
            self.objData = WorkingData(self.df_name)
            logging.debug(self.objData.df.columns)
            logging.debug(self.objData.roadMap.status_checks())
            logging.debug("openData: df_id {}".format(self.objData.id))
        else:
            logging.debug("openData: Data not found")

        return self.objData

    @syslog
    def createUserInterface(self, objUser : UserControl):
        logging.info("Start UserControl 'createUserInterface' function")
        logging.debug("Create obj createInterface." \
                        " Data file name: {}".format(self.df_name))
        self.objIface = Interface(self.df_name, objUser)
        ifaceStatus = self.objIface.printInterface()

        return ifaceStatus

    @syslog
    def startProblemSearch(self):
        logging.info("Start UserControl 'startProblemSearch' function")
        self.objQuality = QualityControl(self.objData)
        resultSearch = self.objQuality.problemSerch()
        logging.debug("UserControl startOfDataProcessing" \
                        "result problem search: {}".format(resultSearch))

    @syslog
    def startProblemSolution(self):
        logging.info("Start UserControl 'startProblemSolution' function")
        
        resultSolution = self.objQuality.problemSolution(resultSearch)
        logging.debug("UserControl startOfDataProcessing" \
                        "result problem solution: {}".format(resultSolution))

    @syslog
    def createTrainAndTestSet(self):
        logging.info("Start UserControl 'createTrainAndTestSet' function")
        
        self.objData.createTrainAndTestSet()

        logging.debug("UserControl startOfDataProcessing" \
                        "Test_set.head(): {}".format(self.objData.test_set.head()))

    @syslog
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
        
        figure = self.objIface.objVisual.createFigure(self.objData)

        return figure

    @syslog
    def main(self, objUser):
        logging.info("Start UserControl 'main' function")
        status = self.createUserInterface(objUser)
        return True

