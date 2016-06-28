# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 11:23:05 2016

@author: foos
"""
import sys
import os
from shutil import copyfile

path2 = []
tpath = []
tpath2 = []
tpath3 = []
for arg in sys.argv[1:]:
    path1 = os.path.abspath(arg)
    path1 = path1.split('/')
    del path1[-1]
    path1 = '/'.join(path1)+'/'
    print "this is path1 :", path1
    with open(arg) as weeded_file :
        lines = weeded_file.readlines()
        f2find = lines
    f2find= f2find[2:]
    for f in f2find:
        path2.append(path1+f[:-1])
    print "this is path2 :", path2
    for p in path2:
        tpath.append(os.path.realpath(p))
    print "this is tpath :", tpath
    for i in tpath:
        index = tpath.index(i)
        tpath2.append(tpath[index].split('/'))
        del tpath2[index][-1]
    print "this is tpath2 :", tpath2
    for i in tpath2:
        index = tpath2.index(i)
        tpath3.append('/'.join(tpath2[index])+'/GXPARM.XDS')
maninput_files = tpath3 

print "this is maninput_files", maninput_files

#### add function to copy file somewhere
j = 0
for i in maninput_files:
    copyfile(i, "./GXPARM"+str(j)+".XDS")
    j+=1