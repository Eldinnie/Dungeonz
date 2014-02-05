'''
Created on 28 jan. 2014

@author: Pieter
'''

class Card(object):
    standards = {"red":"anger","green":"food","purple":"magic","yellow":"play"}
    def __init__(self,color,type="standard"):
        self.color = color
        if type=="standard":
            self.type=self.standards[color]
        else:
            self.type=type

