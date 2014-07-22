# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 14:45:59 2014

@author: proxima1
"""
import os
import sys

class openfile2workwith :
    """this class contain function to open file from tiers software"""
    def openfile:
maninput_files = []
for arg in sys.argv[1:]:
    try:
        if os.path.isfile(arg):
            f = open(arg)
            lines = f.readlines()
            f.close()
            if ("***** XSCALE *****" in lines[1]) and \
               ("elapsed wall-clock time" in lines[-1]):
                maninput_files.append(arg)
            elif ("***** CORRECT *****" in lines[1]) and \
               ("elapsed wall-clock time" in lines[-1]):
                 maninput_files.append(arg)  
    except: 
        pass