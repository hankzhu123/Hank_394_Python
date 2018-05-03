#store into the list of all the numbers, and average 3 each store into new list

"""
Created on Tue Jan 30 17:25:48 2018

@author: Hank
"""

ppmFile = open("check.ppm")

mgicNO = ppmFile.readline()
widthHeight = ppmFile.readline()
widthHeight = widthHeight.split()
max = ppmFile.readline()
p = []

for x in ppmFile :
    l = x.split()
    for a in l:
        p.append(a)


r = p[0 : len(p): 3]
g = p[1 : len(p) : 3]
b = p[2 : len(p): 3]

r = list(map(int, r))
g = list(map(int, g))
b = list(map(int, b))

avgR = [(a + b) / 2 for a, b in zip(r[::2], r[1::2])]
avgG = [(a + b) / 2 for a, b in zip(g[::2], g[1::2])]
avgB = [(a + b) / 2 for a, b in zip(b[::2], b[1::2])]

avgR = list(map(int, avgR))
avgG = list(map(int, avgG))
avgB = list(map(int, avgB))

newRGB = [j for i in zip(avgR, avgG, avgB) for j in i]
#newRGBString = ''.join(str(e) for e in newRGB)

newP = [0] * int((len(p))/2)
pp = 0
i = 0
while (i<len(p)):
    if (i % 6 < 3):
        newP[pp] = (p[i])
        pp = pp + 1
    i = i + 1
    
#newPString = ''.join(str(e)for e in newP)

newW = 128
newH = 256
newFFF = open("newCheck222.ppm", "w")
newFFF.write("%s" % (mgicNO))
newFFF.write("%d %d\n" %(newW, newH))
newFFF.write(max)
    
ii = 0
while (ii < len(newRGB)):
    newFFF.writelines("%s\n" % newRGB[ii])
    ii = ii + 1
    

newFFF.close()
ppmFile.close()



print (max)
