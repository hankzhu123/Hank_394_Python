#Encode message into a ppm pic


import itertools
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
        
width = int(widthHeight[0])
height = int(widthHeight[1])

testS = "Hello World, this is hank speaking!" 
s1 = []

for i in range(len(testS)): #convert text into binary
    ll = ord(testS[i])
    ll = f'{ll:08b}'
    s1.append(ll)

A = [0] * (len(p)//8)
n = 0
for i in range(len(p)//8): #divides original pic into several part, where every part contains 8 numbers
    bb=[]
    for j in range(8):       
        bb.append(p[n])
        n += 1    
    A[i] = bb
#print (A)       


for l in range(len(testS)):
    for i in range(8):#go through testS, 
        s2 = s1[l]
        if (s2[i] == '1' and A[l][i] < 255):          
            A[l][i] += 1
        if (s2[i] == '1' and A[l][i] == 255):
            A[l][i] -= 1
            
            
#print (A)

A = list(itertools.chain(*A)) #convert multi-dimensional list to one d list

#print (A)


newW = width
newH = height
newFFF = open("EncodedBalls.ppm", "w")
newFFF.write("%s" % (mgicNO))
newFFF.write("%d %d\n" %(newW, newH))
newFFF.write(max)
    
zxc = 0
while (zxc < len(A)):
    
    newFFF.writelines("%d\n" % A[zxc])
    zxc = zxc + 1
    

newFFF.close()
ppmFile.close()
        
