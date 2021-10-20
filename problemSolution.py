import numpy as np 
import pandas as pd

from matplotlib import pyplot as plt

import logging
import warnings
warnings.simplefilter('ignore')


class ProblemSolution():

    def __init__(self, df, roadMap):
        self.df = df
        self.roadMap = roadMap

    def reduceMemUsage(self):
        logging.info("Start ProblemSolution 'reduceMemUsage' function")
        logging.debug(self.df)
        for col in list(self.df.columns):
            col_type = self.df[col].dtype

            if col_type != object:
                c_min = self.df[col].min()
                c_max = self.df[col].max()
                if str(col_type)[:3] == 'int':
                    if c_min > np.iinfo(np.int8).min \
                            and c_max < np.iinfo(np.int8).max:
                        self.df[col] = self.df[col].astype(np.int8)
                    elif c_min > np.iinfo(np.int16).min \
                            and c_max < np.iinfo(np.int16).max:
                        self.df[col] = self.df[col].astype(np.int16)
                    elif c_min > np.iinfo(np.int32).min \
                            and c_max < np.iinfo(np.int32).max:
                        self.df[col] = self.df[col].astype(np.int32)
                    elif c_min > np.iinfo(np.int64).min \
                            and c_max < np.iinfo(np.int64).max:
                        self.df[col] = self.df[col].astype(np.int64)
                else:
                    if c_min > np.finfo(np.float16).min \
                            and c_max < np.finfo(np.float16).max:
                        self.df[col] = self.df[col].astype(np.float16)
                    elif c_min > np.finfo(np.float32).min \
                            and c_max < np.finfo(np.float32).max:
                        self.df[col] = self.df[col].astype(np.float32)
                    else:
                        self.df[col] = self.df[col].astype(np.float64)
            else:
                self.df[col] = self.df[col].astype('category')

        end_mem = self.df.memory_usage().sum() / 1024**2
        logging.debug('Memory usage after optimization is: {:.2f} MB'\
                                                        .format(end_mem))
        start_mem = self.roadMap.memory_usage_result[0]
        logging.debug('Decreased by {:.1f}%'.format(100 * \
                                        (start_mem - end_mem) / start_mem))
        self.roadMap.memory_usage_result.append(end_mem)

    def startSolution(self):
        logging.info("Start ProblemSolution 'startSolution' function")
        logging.debug("'startSolution' Data = {}".format(self.df))
        logging.debug("'startSolution' RoadMap = {}".format(self.roadMap))
        if self.roadMap.check_memory_usage is True:
            self.reduceMemUsage()
        return [4, 5, 6]