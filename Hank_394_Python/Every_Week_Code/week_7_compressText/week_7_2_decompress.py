#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 23:48:33 2018

@author: Hank

 decompress the file
"""

ppmFile = open("Compressed_test.txt")

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

newP = []

a = 0
while a < len(p):
    if p[a] == '0': 
        b = int(p[a+1])
        for i in range(b):
            newP.append('0')
        a+=2
    else:
        newP.append(p[a])
        a+=1

print (newP)
        


