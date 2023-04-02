# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 22:59:33 2023

@author: Arusharka Bhattacharya 
"""

from abc import ABC,abstractmethod


class Instrument(ABC):
    @abstractmethod
    def __init__(self,instrument_name,currency):
        self.instrument_name=instrument_name
        self.currency=currency
        
    def is_expired(self):
        pass
    
    def caclualte_price(self):
        pass
        
        

inst1=Instrument("Option","Euro")