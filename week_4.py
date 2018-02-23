ppmFile = open("balls.ppm")

mgicNO = ppmFile.readline()
widthHeight = ppmFile.readline()
widthHeight = widthHeight.split()
max = ppmFile.readline()
p = []

for x in ppmFile :
    l = x.split()
    for a in l:
        p.append(int(a))


r = p[0 : len(p): 3]
g = p[1 : len(p): 3]
b = p[2 : len(p): 3]

r = list(map(int, r))   
g = list(map(int, g))
b = list(map(int, b))

offsetR = [(a + b) / 2 - b for a, b in zip(r[::2], r[1::2])]
offsetG = [(a + b) / 2 - b for a, b in zip(g[::2], g[1::2])]
offsetB = [(a + b) / 2 - b for a, b in zip(b[::2], b[1::2])]

avgR = [(a + b) / 2 for a, b in zip(r[::2], r[1::2])]
avgG = [(a + b) / 2 for a, b in zip(g[::2], g[1::2])]
avgB = [(a + b) / 2 for a, b in zip(b[::2], b[1::2])]

AvgRGB = [j for i in zip(avgR, avgG, avgB) for j in i]
offsetRGB = [j for i in zip(offsetR, offsetG, offsetB) for j in i]

s = 0 
q = int(widthHeight[0])//2*3 #width x128
columnCounter = 0 
newList = []
for columnCounter in range(0, int(widthHeight[1])): #height x128
    for i in range(s, q):
        newList.append(AvgRGB[i])
    for i in range(s, q):
        newList.append(offsetRGB[i]+127.5) #+127.5
    s += int(widthHeight[0])//2*3
    q += int(widthHeight[0])//2*3
 

"""  
newW = int(widthHeight[0])
newH = int(widthHeight[1])
newFFF = open("AveragedWidthWithOffsetsOnTheFarRight_balls.ppm", "w")
newFFF.write("%s" % (mgicNO))
newFFF.write("%d %d\n" %(newW, newH))
newFFF.write(max)
    
ii = 0
while (ii < len(newList)):
    
    newFFF.writelines("%d\n" % newList[ii])
    ii = ii + 1
    

newFFF.close()
ppmFile.close()

"""
rr = []
bb = []
gg = []

offsetRl = []
offsetGl = []
offsetBl = []

width = int(widthHeight[0])

for i in range(int(int(widthHeight[1])/2)): #here i is which set of rows
    #print("final:",i,i*width*3*2)
    for j in range(int(width)): # j is which color in that row
        #print(j,i*width*3*2 + 3*j)
        firstr = i*(width)*3*2 + 3*j
        firstg = firstr + 1
        firstb = firstr + 2
        secondr = i*(width)*3*2 + 3*j + 3*(width)
        secondg = secondr + 1
        secondb = secondr + 2
        
        rl = int((newList[firstr] + newList[secondr])/2)
        bl = int((newList[firstb] + newList[secondb])/2)
        gl = int((newList[firstg] + newList[secondg])/2)
        
        offsetRR = rl - newList[secondr] + 127.5
        offsetBB = bl - newList[secondb] + 127.5
        offsetGG = gl - newList[secondg] + 127.5
        
        rr.append(rl)
        bb.append(bl)
        gg.append(gl)
        
        offsetRl.append(offsetRR)
        offsetGl.append(offsetGG)
        offsetBl.append(offsetBB)
                
        
        #print (i, j, secondr)
        #print(firstr,firstg,firstb,secondr,secondg,secondb)
       
newRGB = [j for i in zip(rr, gg, bb) for j in i]
offsetRGB = [j for i in zip(offsetRl, offsetGl, offsetBl) for j in i]
#print (offsetRl)       
        
RGB = newRGB + offsetRGB

#print (rr)


newW = int(widthHeight[0])
newH = int(widthHeight[1])
newFFF = open("AveragedHeightWithOffsetsOnTheBottom_balls.ppm", "w")
newFFF.write("%s" % (mgicNO))
newFFF.write("%d %d\n" %(newW, newH))
newFFF.write(max)
    
ii = 0
while (ii < len(RGB)):
    
    newFFF.writelines("%d\n" % RGB[ii])
    ii = ii + 1
    

newFFF.close()
ppmFile.close()
