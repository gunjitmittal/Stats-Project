import numpy as np 
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import numpy as np



#compute areas for differnet for values of Z in standard normal

df=pd.read_excel(r'C:\Users\HP\Downloads\preprocessed_data.xlsx')
df=np.array(df)


Y1=df[:,13]
Y2=df[:,7]
Y1.sort()
Y2.sort()
Y3=df[:,8]
Y3.sort()



#sample size
n=len(df)
print(n)
X=np.zeros(n)
# print(stats.norm.ppf(0.05,loc=0,scale=1))
for i in range(0,n):
 X[i]=stats.norm.ppf((i+1-0.5)/n, loc=0, scale=1)


plt.title('QQ plot')
plt.xlabel('money')
plt.ylabel('standard normal')
plt.scatter(Y1,X)
plt.grid()
plt.show()


# Get the slope and intercept of the line
m = 0.40
c = -1.30

linex=np.linspace(0,17,num=50)
liney=m*linex+c
print(m,c)

plt.title('QQ plot')
plt.xlabel('no of hours in a stretch')
plt.ylabel('standard normal')
plt.plot(linex,liney)
plt.scatter(Y2,X)
plt.grid()
plt.show()

print("new")
X=X.astype('float')
Y2=Y2.astype('float')
coefficient=np.polyfit(Y2,X,1)
print(coefficient[0],coefficient[1])

#correlation coeeficient
meanx=np.sum(X,axis=0)/n
meany1=np.sum(Y1,axis=0)/n

meany2=np.sum(Y2,axis=0)/n

print(meanx,meany1,meany2)

sdx=0
sdy1=0
sdy2=0

print(stats.pearsonr(Y1,X))
print(stats.pearsonr(Y2,X))


#0.4136360902808279 -1.310276319971472 