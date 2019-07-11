#3504 mini-project #1
#Alan Kan

import pandas as pd
import numpy as np
import xlrd
import matplotlib.pyplot as plt
import math

data = pd.read_excel("/Users/alankan/Documents/UConn/Spring 2018/CSE 3504/mini-project1-data.xlsx")


QiSum = [[0 for i in range(len(data.keys())+1)]for j in range(6)]


Qnum = 1
for key in data.keys():
    for values in data[key]:
        QiSum[values][Qnum]+=1
    Qnum+=1

#Task 1
#1-1

PQi = [[0 for i in range(len(data.keys())+1)] for j in range(6)]

for rows in range(1,6):
    for colns in range(1, len(QiSum[0])):
        PQi[rows][colns] = QiSum[rows][colns]/sum([i[colns] for i in QiSum][1:6])


l=['Q'+str(i) for i in range(27)]

count=1
j=1
for i in range(1,27):
    for Qs in PQi[1:6]:
        print(l[i] + ' '+'response'+' '+str(j)+' '+'probability'+' '+'is',Qs[count])
        j+=1
    print('\n')
    j=1
    count+=1

#1-2

for i in range(1,27):
    plt.bar([1,2,3,4,5],[row[i] for row in PQi][1:6], align='center')
    plt.title(l[i])
    plt.xlabel('Responses')
    plt.ylabel('Probability')
    plt.show()

#Task 2
#2-1
#mean


Qsum=[]
for keys in data.keys():
    for values in data[keys]:
        if values != 0:
            Qsum.append(values)
    print(keys+' '+'Mean is'+' ',np.mean(Qsum))
    Qsum=[]

print('\n')

#variance

varsum = []
for keys in data.keys():
    for values in data[keys]:
        if values !=0:
            varsum.append(values)
    print(keys+' '+'Variance is'+' ', np.var(varsum))
    varsum=[]

print('\n')
#Entropy

count= 1
Esum = 0
for i in range(1, 27):
    for Qs in PQi[1:6]:
        Esum += -Qs[count]*math.log(Qs[count],2)
    count+=1
    print(l[i]+' '+'Entropy is'+' ', Esum)
    Esum=0
          
#Task 3

dist ={}

Qx = ['Q'+str(i) for i in range(27)][1:]

Q=[]
z= 1
for i in Qx:
    for j in Qx[z:]:
        Q.append(str(i)+str(j))
    z+=1

for i in Q:
    dist[i] = 0

Hsum = 0
Hval = 0
for i in Q:
    Hsum=0
    for Qs in PQi[1:6]:
        if len(i) ==4:
            A = int(i[1])
            B = int(i[3])
            Hsum+=(math.sqrt(Qs[A]) - math.sqrt(Qs[B]))**2
        elif len(i) == 5:
            A = int(i[1])
            B = int(i[3:])
            Hsum+=(math.sqrt(Qs[A]) - math.sqrt(Qs[B]))**2
        elif len(i) == 6:
            A = int(i[1:3])
            B = int(i[4:])
            Hsum += (math.sqrt(Qs[A]) - math.sqrt(Qs[B]))**2
    Hval = (1/math.sqrt(2)) * math.sqrt(Hsum)
    dist[i] = Hval
  #  Hsum = 0
    
#print(dist)
    #3.
l2=[]
zzz =list(dist.keys())
yyy = list(dist.values())

for values in dist.values():
    l2.append(values)
print("The highest Hellinger distance pair is", zzz[yyy.index(max(l2))], "with a value of", max(l2))
print("The Lowest Hellinger distance pair is ", zzz[yyy.index(min(l2))], "with a value of", min(l2))

    #4.

#print(zzz)
#print(yyy)
plt.bar(zzz,yyy, align='center')
plt.title('Spread of Hellinger distances')
plt.xlabel('pairs')
plt.ylabel('Hellinger distances')
plt.show()
