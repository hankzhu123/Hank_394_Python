#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 16:46:00 2018

@author: Hank

    compress the file
"""

ppmFile = open("test_rwv1.txt")

mgicNO = ppmFile.readline()
widthHeight = ppmFile.readline()
widthHeight = widthHeight.split()
max = ppmFile.readline()
p = []

for x in ppmFile :
    l = x.split()
    for a in l:
        p.append(a)
        
width = int(widthHeight[0])
height = int(widthHeight[1])

#threshold = input("What is your theshold? ")
#type(threshold)

threshold = 1.5

newL = []
newL2 = []

#print (p)

for l in range(len(p)):
    if (int(float(p[l])) < threshold):
        newL.append(0)
    else:
        newL.append(int(float(p[l])))


i = 0
while i < len(newL):

    if newL[i] == 0:       
        j = 1        
        while i+j < len(newL) and newL[i+j] == 0:
            j += 1
        newL2.append(0)
        newL2.append(j)
        #print (j)
        i = i + j
       
    else:
        newL2.append(newL[i])
        #print (newL[i])
        i = i + 1
    

newW = width
newH = height
newFFF = open("Compressed_test.txt", "w")
newFFF.write("%s" % (mgicNO))
newFFF.write("%d %d\n" %(newW, newH))
newFFF.write(max)
    
zxc = 0
while (zxc < len(newL2)):
    
    newFFF.writelines("%d\n" % newL2[zxc])
    zxc = zxc + 1
    

newFFF.close()
ppmFile.close()
    
    
    
    

   
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
