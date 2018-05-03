#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 20:47:27 2018

@author: Hank
"""

ppmFile = open("AveragedHeightWithOffsetsOnTheBottom_balls.ppm")

mgicNO = ppmFile.readline()
widthHeight = ppmFile.readline()
widthHeight = widthHeight.split()
max = ppmFile.readline()
p = []

for x in ppmFile :
    l = x.split()
    for a in l:
        p.append(int(a))
        
width = int(widthHeight[0])
height = int(widthHeight[1])
        
fOffset = (height // 2) * width * 3#first number of first line of offset

#sLine = int(width) #first number of second line of avg

# p[0] - p[fOffset]

oddLine = []
evenLine = []
i = 0

for l in range(height//2):
    for z in range(width*3): #rgb
        q = p[i] - (p[fOffset+i] - 127)#avg - offset = oddLine#
        #r = 2*p[i] - q #evenLine#
        r = p[i] + (p[fOffset+i] - 127)
        oddLine.append(q)
        evenLine.append(r)
        i += 1

#print(evenLine)
#print(oddLine)

m1 = 0
m2 = 0
i = 0
OffsetOnTheRight = []

    
while(i < height):
    if(i % 2 == 1):
        for il in range(width*3):
            OffsetOnTheRight.append(oddLine[m2])
            m2 += 1
    if(i % 2 == 0):
        for il in range(width*3):
            OffsetOnTheRight.append(evenLine[m1])
            m1 += 1
    i +=1        
  
#print (OffsetOnTheRight)
       
        
#fOffset2 = width * 3 // 2 #first offset

#sOffset2 = fOffset2 + width * 3 #second line of first offset

OldPic = []
firstHalf = []
secondHalf = []
iop = 0
print(width,height)
for asd in range(height):
    for qwe in range(width//2*3):
        iop = asd*width*3 + qwe
        sHalf = OffsetOnTheRight[iop] - (OffsetOnTheRight[iop+width//2*3] - 127) #get second half of line  
        secondHalf.append(sHalf)
       # fHalf = 2*p[iop] - sHalf #get first half of line   
        fHalf = OffsetOnTheRight[iop] +  OffsetOnTheRight[iop+width//2*3] - 127
        firstHalf.append(fHalf)
        iop += 1
print("iop",iop)
wer = 0
for bnm in range(height):
    for jkl in range(width//2):
            for mno in range(3):
                OldPic.append(firstHalf[wer + mno])
            for mno in range(3):
                OldPic.append(secondHalf[wer + mno])
            wer += 3
print("wer",wer)
newW = width
newH = height
newFFF = open("OldPic_Balls.ppm", "w")
newFFF.write("%s" % (mgicNO))
newFFF.write("%d %d\n" %(newW, newH))
newFFF.write(max)
    
zxc = 0
while (zxc < len(OldPic)):
    
    newFFF.writelines("%d\n" % OldPic[zxc])
    zxc = zxc + 1
    

newFFF.close()
ppmFile.close()
