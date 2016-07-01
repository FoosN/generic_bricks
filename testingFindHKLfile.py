# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 11:46:06 2016

@author: foos
"""

import sys
import os


USAGE = """ USAGE: %s [OPTION] <path to the directory of interest>
 
OPTIONS : -HKL : file to use are HKL file from XSCALE program (script scan directory
to find them)
         -W : file input is weeded_file.txt written by G.A 
         -G : file input are GXPARM.XDS (script scan directory to find them) """


if len(sys.argv) == 1:
    print USAGE
    quit()
    


def StartingOpen(): 
    maninput_files = []  
    if len(sys.argv[1:]) >= 1:
        if sys.argv.count("-HKL"):
            sys.argv.remove("-HKL")
            option = "HKL"
        else :
            option = "NO_opt"
        if sys.argv.count("-W"):
            sys.argv.remove("-W")
            option = "weeded_file"
        else :
            option = "NO_opt"
        if sys.argv.count("-G"):
            sys.argv.remove("-G")
            option = "GXPARM"
        else : 
            option = "NO_opt"
        #return listofOptions
#    else :
#        option = None
        
    if option is "HKL":
        TTTTTTT= "truc a faire"
    elif option is "weeded_file":
        path2 = []
        tpath = []
        tpath2 = []
        tpath3 = []
        for arg in sys.argv[1:]:
            try:
                if arg == "weeded_files.txt":
                    path1 = os.path.abspath(arg)
                    path1 = path1.split('/')
                    del path1[-1]
                    path1 = '/'.join(path1)+'/'
                    with open(arg) as weeded_file :
                        lines = weeded_file.readlines()
                        f2find = lines
                    f2find=f2find[2:]
                    for f in f2find:
                        path2.append(path1+f[:-1])
                    for p in path2:
                        tpath.append(os.path.realpath(p))
                    for i in tpath:
                        index = tpath.index(i)
                        tpath2.append(tpath[index].split('/'))
                        del tpath2[index][-1]
                    for i in tpath2:
                        index = tpath2.index(i)
                        tpath3.append('/'.join(tpath2[index])+'/GXPARM.XDS')
                    maninput_files = tpath3 
            except:
                pass
    elif option is "GXPARM":
        for arg in sys.argv[1:]:
            path= os.path.abspath(arg)
        for root, dirs, files in os.walk(path):
            for filename in files:
                if "GXPARM" and ".XDS" in filename:
                    maninput_files.append(os.path.join(root, filename))
    elif option is "NO_opt":
        message1 = "please define option to precise which type of file you want to use"
        quit()
    else :
        message1 = "Error occured, verify your command line"
        quit()
    if message1 :
        print message1
        quit()
    else :
        print maninput_files
        
    return maninput_files, option
    
maninput_files=StartingOpen()
print maninput_files

