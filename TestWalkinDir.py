# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 15:51:06 2016

@author: foos
"""
import sys
import os

maninput_files = []
for arg in sys.argv[1:]:
    path= os.path.abspath(arg)
for root, dirs, files in os.walk(path):
    for filename in files:
        if filename == "GXPARM.XDS":
            maninput_files.append(os.path.join(root, filename))
            
print "ok this is maninput :" + str(maninput_files)