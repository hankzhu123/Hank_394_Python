#store into the list of all the numbers, and average 3 each store into new list

"""
Created on Tue Jan 30 17:25:48 2018

@author: Hank
"""

ppmFile = open("colors.ppm")

mgicNO = ppmFile.readline()
widthHeight = ppmFile.readline()
widthHeight = widthHeight.split()

p = []

for x in ppmFile :
    l = x.split()
    for a in l:
        p.append(a)


r = p[0 : len(p)-1 : 3]
g = p[1 : len(p)-1 : 3]
b = p[2 : len(p)-1 : 3]

r = list(map(int, r))
g = list(map(int, g))
b = list(map(int, b))

avgR = [(a + b) / 2 for a, b in zip(r[::2], r[1::2])]
avgG = [(a + b) / 2 for a, b in zip(g[::2], g[1::2])]
avgB = [(a + b) / 2 for a, b in zip(b[::2], b[1::2])]

newRGB = [j for i in zip(avgR, avgG, avgB) for j in i]

newP = [0] * int((len(p)-1)/2)
pp = 0
i = 0
while (i<len(p)-1):
    if (i % 6 < 3):
        newP[pp] = (p[i])
        pp = pp + 1
    i = i + 1



print (widthHeight)
