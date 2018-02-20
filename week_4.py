ppmFile = open("AveragedWidthWithOffsetsOnTheFarRight.ppm")

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
        newList.append(offsetRGB[i] + 127.5)
    s += int(widthHeight[0])//2*3
    q += int(widthHeight[0])//2*3


rr = []
bb = []
gg = []

offsetRl = []
offsetGl = []
offsetBl = []

for i in range(int(int(widthHeight[1])/2)): #here i is which set of rows
    #print("final:",i,i*width*3*2)
    for j in range(int(widthHeight[0])): # j is which color in that row
        #print(j,i*width*3*2 + 3*j)
        firstr = i*(int(widthHeight[0]))*3*2 + 3*j
        firstg = firstr + 1
        firstb = firstr + 2
        secondr = i*(int(widthHeight[0]))*3*2 + 3*j + 3*(int(widthHeight[0]))
        secondg = secondr + 1
        secondb = secondr + 2
        
        rl = int((newList[firstr] + newList[secondr])/2)
        bl = int((newList[firstb] + newList[secondb])/2)
        gl = int((newList[firstg] + newList[secondg])/2)
        
        offsetRR = rl - newList[secondr]
        offsetBB = bl - newList[secondb]
        offsetGG = gl - newList[secondg]
        
        rr.append(rl)
        bb.append(bl)
        gg.append(gl)
        
        offsetRl.append(offsetRR)
        offsetGl.append(offsetGG)
        offsetBl.append(offsetBB)
                
   
        
        
        #print (i, j, secondr)
        #print(firstr,firstg,firstb,secondr,secondg,secondb)
       
#newRGB = [j for i in zip(rr, gg, bb) for j in i] #average between rows 
#print (offsetRl)
        
        
RGB = []
count = 0
count2 = 0
for i in range(int(widthHeight[1])): 
    if (i % 4 < 2):
        for ii in range(int(widthHeight[0])):
            RGB.append(rr[count])
            RGB.append(gg[count])
            RGB.append(bb[count])
            count += 1
    else:
        for ii in range(int(widthHeight[0])):
            RGB.append(offsetRl[count2])
            RGB.append(offsetGl[count2])
            RGB.append(offsetBl[count2])
            count2 += 1
                
#print (RGB)

newW = int(widthHeight[0])
newH = int(widthHeight[1])
newFFF = open("Averaged Height with offsets on the bottom.ppm", "w")
newFFF.write("%s" % (mgicNO))
newFFF.write("%d %d\n" %(newW, newH))
newFFF.write(max)
    
ii = 0
while (ii < len(RGB)-3):
    
    newFFF.writelines("%d\n" % RGB[ii])
    ii = ii + 1
    

newFFF.close()
ppmFile.close()

