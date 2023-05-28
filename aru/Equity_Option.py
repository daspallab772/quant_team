# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 16:39:55 2023

@author: Win10
"""

from Option_new import Option

class Equity_Option(Option):
    def _init_(self,stock,dividend,interestrate):
        super._init_()
        self.stock=stock
        self.dividend=dividend
        self.interestrate=interestrate
        
    def is_expired(self):
        Option.is_expired(self)
        
    def calculate_price(self):
        pass
    
    def greeks_calculation(self):
        pass
    
    def forward_price(self):
        pass
    

    
