#!/bin/python3

class Colors:
    def __init__(self, intF=None, intB=None):
        self.intF = "37"
        self.intB = "40"

    def out(self, stringa='', intF=None, intB=None):
        self.setting( intF,intB )
        print( "\033["+ self.intF +";"+ self.intB +"m", stringa, end='', sep='' )
        print( "\033[37;40m", end='' )

    def setting(self,intF=None,intB=None):
        if   intF == 30: self.intF = "30" #black
        elif intF == 31: self.intF = "31" #red
        elif intF == 32: self.intF = "32" #green
        elif intF == 33: self.intF = "33" #yellow
        elif intF == 34: self.intF = "34" #blue
        elif intF == 36: self.intF = "36" #Cyan
        elif intF == 96: self.intF = "96" #light-blue
        else: self.intF = "37" #white

        if   intB == 31: self.intB = "41"  #red
        elif intB == 32: self.intB = "42"  #green
        elif intB == 33: self.intB = "43"  #yellow
        elif intB == 34: self.intB = "44"  #blue
        elif intB == 36: self.intB = "46"  #Cyan
        elif intB == 37: self.intB = "47"  #white
        elif intB == 96: self.intB = "106" #light-blue
        else: self.intB = "40" #black
