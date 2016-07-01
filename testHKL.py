# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:25:06 2016

@author: foos
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import sys
import os
import glob
import numpy as np


# case where file are .HKL from XSCALE (typical output of GA grouping step)
maninput_files = []
for arg in sys.argv[1:]:
    path= os.path.abspath(arg)
files = glob.glob("*.HKL")
if files is True:
    MyFile = "HKL file"
    for filename in files:
        maninput_files.append(os.path.join(path, filename))
crystList = []
table = []
table1 = []
table2 = []
if MyFile == "HKL file":
    for i in maninput_files :
        with open(i) as inputfile:
            for line in inputfile:
                if "UNIT_CELL_A-AXIS=" in line:
                    axeA = line 
                if "UNIT_CELL_B-AXIS=" in line:
                    axeB = line
                    #table.append(line[18:])
                if "UNIT_CELL_C-AXIS=" in line:
                    axeC = line                    
                    table=axeA[18:], axeB[18:], axeC[18:]
            table1.append(table)
        for i in table1:
            vecta = i[0].split()
            vectb = i[1].split()
            vectc = i[2].split()
            vecta2 = np.array([float(vecta[0]), float(vecta[1]), float(vecta[2])])
            vectb2 = np.array([float(vectb[0]), float(vectb[1]), float(vectb[2])])
            vectc2 = np.array([float(vectc[0]), float(vectc[1]), float(vectc[2])])
        vectRes = vecta2+vectb2+vectc2
        crystList.append(vectRes)








vectMagn = []
for i in crystList:
    magn=np.sqrt(np.vdot(i,i))
    vectMagn.append(magn)
fig = plt.figure()
ax = fig.add_subplot(111)
for i in vectMagn:
    ax.scatter(vectMagn.index(i), [i], c='r', marker= '^')
plt.show()
########    create the list of vector 2D from the crystList (contain 3D vector)
#
#vector2D=[]
#for i in crystList:
#    vector2D.append([0,0,i[0],i[1]])
#
#vector = np.array(vector2D)
#X,Y,U,V = zip(*vector)
#plt.figure()
#ax = plt.gca()
#ax.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1)
#ax.set_xlim([np.amin(U)-10,np.amax(U)+10])
#ax.set_ylim([np.min(V)-10,np.amax(V)+10])
#plt.draw()
#plt.show()
#
#######    3D plot scattering. (using Sum vector from crystList)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#for i in crystList:
#    ax.scatter(i[0], i[1], i[2], c='y', marker='d')
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Z')
#
#plt.show()  
#
#########    2D plot scattering (using Sum vector orthogonal projection along z)
#fig = plt.figure()
#ax = fig.add_subplot(111)
#for i in crystList:
#    ax.scatter(i[0], i[1], c='b', marker='o')
#plt.show()


####### 3D plot vectors
vector3D=[]
for i in crystList:
    N = np.sqrt(np.vdot(i,i))
    vector3D.append([0,0,0,i[0],i[1],i[2], N])
#
######## WARNING : magnitude for represented vectors is arbitraty parametered see following :
#lenVect = np.average(N)
vector = np.array(vector3D)
#X,Y,Z,U,V,W,N = zip(*vector)
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#s = ax.quiver(X,Y,Z,U,V,W, length = lenVect, colors='b', arrow_length_ratio=0.05, pivot='middle')
##ax.quiver(X,Y,Z,U,V,W,W, cmap=plt.cm.gray, arrow_length_ratio=0.05, zorder=4, pivot='middle')'
#ax.set_xlim([-lenVect-10, lenVect+10])
#ax.set_ylim([-lenVect-10, lenVect+10])
#ax.set_zlim([-lenVect-10, lenVect+10])
#ax.patch.set_facecolor('0.7')
#
#plt.draw()
#plt.show()
#
#
##### export table with vector for pymol
#print "this is the table of vector : ", vector3D

def writing_list_in_file(path, file2write):
    outputfile = open(os.path.join(path, "arrow4pymol.txt"), 'a')
    for line in file2write:    
        outputfile.write("cgo_arrow "+line+'\n')

file2write = []
for i in vector3D: 
    coord = '['+str(i[0]-0.5*i[3])+','+str(i[1]-0.5*i[4])+','+str(i[2]-0.5*i[5])+'],['+str(0.5*i[3])+','+str(0.5*i[4])+','+str(0.5*i[5])+']'
#    coord = '['+str(i[0])+','+str(i[1])+','+str(i[2])+'],['+str(i[3])+','+str(i[4])+','+str(i[5])+']'
    file2write.append(coord)

writing_list_in_file(".", file2write)
    

         
