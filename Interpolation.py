# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 13:43:53 2023

@author: Win10
"""

class Interpolation:
    def __init__(self):
        pass
    
    def linearinterpolation(self,d,x):
        Output = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0]))