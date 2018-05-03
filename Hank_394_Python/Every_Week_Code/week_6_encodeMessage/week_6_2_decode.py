#Decoding the message from ppm

ppmFile = open("EncodedBalls.ppm")

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

ppmFile2 = open("balls.ppm")

mgicNO2 = ppmFile2.readline()
widthHeight2 = ppmFile2.readline()
widthHeight2 = widthHeight2.split()
max2 = ppmFile2.readline()
p2 = []

for x in ppmFile2 :
    l = x.split()
    for a in l:
        p2.append(int(a))
        
width2 = int(widthHeight2[0])
height2 = int(widthHeight2[1])

p3 = []
for i in range(len(p)): #find the difference between two list, store in p3
    a = abs(p[i]-p2[i])
    p3.append(a)

#print (p3)

A = [0] * (len(p3)//8)
n = 0
for i in range(len(p3)//8): #divides p3 into several part, where every part contains 8 numbers
    bb=[]
    for j in range(8):       
        bb.append(p3[n])
        n += 1    
    A[i] = bb
#print (A)

B = []
for i in range(len(A)):
    bi = str(''.join(map(str,A[i])))
    if (bi == '00000000'):
        break
    else:
        de = int(bi, 2)
        ch = chr(de)
        B.append(ch)
        
word = str(''.join(map(str,B)))

print (word)











