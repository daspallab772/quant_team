# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 00:18:10 2023

@author: Arusharka Bhattacharya 
"""

from enum import Enum,unique

@unique
class currency(Enum):
       USD='USD'
       EUR='EUR'
       GBP='GBP'
       INR='INR'
       CAD='CAD'
       AUD='AUD'
       SGD='SGD'
       YEN='YEN'
       
     
        
@unique
class compoundingtype(Enum):
       Simple='Simple'
       Annual='Annual'
       SemiAnnual='SemiAnnual'
       Quarterly='Quarterly'
       Continuous='Continuous'
       

@unique
class interpolationtype(Enum):
        Linear='Linear'
        LogLinear='Loglinear'
        Cubic='Cubic'
        Quadratic='Quadratic'
       