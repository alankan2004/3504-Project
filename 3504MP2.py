#3504 mini-project #2

import pandas as pd
import numpy as np
import xlrd
import matplotlib.pyplot as plt
import math

data = pd.read_excel("/Users/alankan/Documents/UConn/Spring 2018/CSE 3504/mini-project2/mini-project2-data-v3.xlsx")

#Task1

FemaleSum = [[0 for i in range(len(data.keys()))]for j in range(6)]
MaleSum = [[0 for i in range(len(data.keys()))] for j in range(6)]


Qnum = 1

ttlavg=[]
avgM =[]
avgF =[]
for key in data.keys():
    if key != "gender":
        index = 0
        lofMale=[]
        lofFe =[]
        lofTtl=[]
        for values in data[key]:
            
            if data['gender'][index] == 1:
                FemaleSum[values][Qnum]+=1
                if values != 0:
                    lofFe.append(values)
            elif data['gender'][index] == 2:
                MaleSum[values][Qnum]+=1
                if values != 0:
                    lofMale.append(values) #for task3 mean
            if values != 0:
                lofTtl.append(values)
            index+=1
        if lofFe is not None:
            avgF.append(np.mean(lofFe))
        if lofMale is not None:
            avgM.append(np.mean(lofMale))
        ttlavg.append(np.mean(lofTtl))
        Qnum+=1
                       
           
##print(FemaleSum)
##print('\n')
##print(MaleSum)
#print(avgM)
#print(avgF)


print('\n')
Female =[]
Male=[]
for i in range(1,27):
    Female.append([row[i] for row in FemaleSum])
    Male.append([row[i] for row in MaleSum])
##print(Female)
##print(Male)


print('\n')

ttlrep = []
for i in range(0,26):
    plug = Female[i][1:6]
    for j in (Male[i][1:6]):
        plug.append(j)
    ttlrep.append(plug)
 #   print(plug)
    plt.bar(['F1','F2','F3','F4','F5','M1','M2','M3','M4','M5'], plug, align='center')
    plt.title('Female vs Male distribution for Q'+str(i+1))
    plt.xlabel('Female Responses and Male Responses')
    plt.ylabel('Number of responses')
 #   plt.show()


#Task2

#print(ttlrep)
fProb =[]#female probabilities
for resl in range(0,26):
    result=[]
    for respon in range(0,5):
        total = ttlrep[resl][respon]
        prob = total/1411
        result.append(prob)
    fProb.append(result)

#prob is the list questions of list of probablilties of responses 1-5
#print(fProb,'\n')


#male probabilities
mProb=[]
for resl in range(0,26):
    result=[]
    for respon in range(5,10):
        total = ttlrep[resl][respon]
        prob = total/1411
        result.append(prob)
    mProb.append(result)

#print(mProb,'\n')

for Qs in range(0, 26):
    sumup =0
    for i in range(0,5):
        sumup+= (math.sqrt(mProb[Qs][i]) - math.sqrt(fProb[Qs][i]))**2
    hellinger = (math.sqrt(sumup)) / math.sqrt(2)
    print('The Hellinger distance of Q'+str(Qs+1) + ':', hellinger)

#Task3

#we are having the male avg - female avg then minus 0, and have that divide by sqrt(overall avg * (1 - overall proportion) *(1/number of male responses + 1 / male responses)

#overall avg


for i in range(0, 26):
    #z = (avgM[i] - avgF[i] - 0)/math.sqrt(ttlavg[i]*(1 - ttlavg[i])* ( (1/len(avgM)) + (1/len(avgF))))
    num = avgM[i] - avgF[i] - 0
    denum = math.sqrt(abs(ttlavg[i]*(1 - ttlavg[i])*(1/len(avgM) + (1/len(avgF)))))
    z = num/denum
    print("Z for Q"+str(i+1)+' is', z)
print("ttlavg", ttlavg)
#print(avgM)
#print(avgF)

##for i in range(0,26):
##    print('Difference between avgM and avgF for Q'+str(i+1)+' is', abs(avgM[i]-avgF[i]))



#calculating seprate standard deviation, one for male and one for female each Question

fValues=[]
mValues=[]
for key in data.keys():
    if key!='gender':
        index=0
        fV=[]
        mV=[]
        for values in data[key]:
            if data['gender'][index] == 1 and values != 0:
                fV.append(values)
            elif data['gender'][index] == 2 and values != 0:
                mV.append(values)
            index+=1
        if fV is not None:
            fValues.append(fV)
        if mV is not None:
            mValues.append(mV)

#print(len(mValues[0]))
print('\n')
#print(len(fValues[0]))

#male

for i in range(0,26):
    res=0
    index = len(mValues[i])
    for j in range(0,index):
        res += (mValues[i][j]- avgM[i])**2
    ttl = res * (1/index)
   # print("The standard deviation for Q"+ str(i+1)+' is', math.sqrt(ttl))
    
print('\n')

#female
for i in range(0,26):
    res=0
    index = len(fValues[i])
    for j in range(0, index):
        res += (fValues[i][j] - avgF[i])**2
    ttl = res *(1/index)
    #print("The standard deviation for Q"+str(i+1)+' is', math.sqrt(ttl))

#so we assume H0 <=1 , H1 > 1, we seek to show the z-score, 
