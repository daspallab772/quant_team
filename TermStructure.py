# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 01:00:13 2023

@author: Win10
"""

from abc import ABC,abstractmethod

from datetime import date

from LibraryEnum  import interpolationtype;

class Termstructure ():
    def __init__(self,dates:list(),interestrate:list(),interpolator:interpolationtype):
        assert len(dates)==len(interestrate), "length of dates does not match with lengh of interestrate"
        
        self.dates=dates
        self.interestrate=interestrate
        self.interpolator=interpolator
        
        
        
date1=date(2021,3,12)
date2=date(2021,3,13)
date3=date(2021,3,14)

interestrate1=0.0496
interestrate2=0.0497
interestrate3=0.0498

dates=[date1,date2,date3]

interestrate=[interestrate1,interestrate2,interestrate3]

mytermstructure=Termstructure(dates, interestrate, interpolationtype.Linear)
