from __future__ import annotations

import logging
import warnings
warnings.simplefilter('ignore')


from problemSearch import ProblemSearch
from problemSolution import ProblemSolution


class QualityControl():

    def __init__(self, objData : OpenData):
        self.df = objData.df
        self.roadMap = objData.roadMap

    def problemSerch(self):
        logging.info("Start QualityControl 'problemSerch' function")
        problemData = ProblemSearch(self.df, self.roadMap)
        result = problemData.startSearch()
        logging.debug("'problemSerch' obj_source {}"\
                                        .format(problemData.df.head()))
        return result

    def problemSolution(self, data):
        logging.info("Start QualityControl 'problemSolution' function")
        logging.debug("'problemSolution' data = {}".format(data))
        obj_Solution = ProblemSolution(self.df, self.roadMap)
        result = obj_Solution.startSolution()
        return result