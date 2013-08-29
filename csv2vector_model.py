# -*- coding: utf-8 -*-

import csv, os

from qgis.core import *

class Csv2vectorModel(object):
    def __init__(self, ):
        self.csvFilePath = None;
        self.shpFilePath = None;
        self.shpFileEncoding = None;
        self.csvDelimiter = None;
    def recalculateCoordinates(self, (x,y), azGrad, dist):
        import math
        azRad = math.pi * azGrad / 180
        return (x+math.sin(azRad)*dist, y+math.cos(azRad)*dist)
    