# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 19:44:20 2018

@author: Samiksha Agarwal
"""

#%%
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from collections import defaultdict
import operator

#%%

data=[[7,11,-1],[15,9,-1],[15,7,-1],[13,5,-1],[14,4,-1],[9,3,-1],[11,3,-1],[11,11,1],[13,11,1],[8,10,1],[9,9,1],[7,7,1],[7,5,1],[15,3,1]]
data=pd.DataFrame(data)
data.columns=["A1","A2","Label"]
#%%
train ,test = train_test_split(data,test_size=0.25,random_state=0)
#%%
def euclidean_distance(point, centroid):
    return np.sqrt(np.sum((point - centroid)**2))

#%%
def KNN(train,test,K):
    distance=[]
    for i in range(len(test)):
        dis=defaultdict(int)
        a=np.asarray(test.iloc[i:i+1,:2])
        for j in range(len(train)):
            b=np.asarray(train.iloc[j:j+1,:2])
            d=euclidean_distance(a,b)
            dis[j]+=d
        dis=sorted(dis.items(), key=operator.itemgetter(1))
        distance.append(dis)
    k={}
    u=0
    for i in distance:
        a=i[:K]
        k[u]=a
        u+=1
       # print(a)
    return k
#%%
def S(Xi,Xj):
    if Xi > Xj:
        return 1
    elif Xi == Xj:
        return 0.5
    else:
        return 0

#%%
ss=KNN(train,test,3)
n=0
index={}
for i in ss.values() :
    qq=[]
    for j in i:
        a=j[0]
        qq.append(a)
        print(qq)
    index[n]=qq 
    n+=1
#%%
score=[]
for i in index.values():
    count=0
    for j in i:
        l= train.iloc[j,-1]
        if l==1:
            count+=1
    print(count,len(i))
    value=count/len(i)
    score.append(value)        
#%%
test['score']=score
pos_test=test[test["Label"]==1]
neg_test=test[test["Label"]==-1]
#%%
auc=0
for i in pos_test.iloc[:,-1]:
    for j in neg_test.iloc[:,-1]:
        s=S(i,j)
        #print(s)
        auc+=s
auc=auc/len(test)    
#%%

print("Test Data with their score values", test) 
print("===================================")
print("AUC value", auc)   
        
        
        
    
        
        
    
