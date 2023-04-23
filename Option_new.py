# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 14:52:41 2023

@author: Win10
"""
import Instrument

from LibraryEnum import currency

from datetime import date, datetime

class Option(Instrument):
    def __init__(self, payoffs:list,maturityDate:date(),valuationDate:date()):
        super._init()
        self.payoffs=payoffs
        self.maturityDate=maturityDate
        self.valuationDate=valuationDate
        
             
    def is_expired(self):
        
        try:
            self.maturityDate>self.valuationDate
        except:
            print("valudation date can not exceed the maturity date")
    
    
    def caclualte_price(self):
        pass
    
    