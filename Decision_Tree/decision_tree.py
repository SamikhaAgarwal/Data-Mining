# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 23:04:23 2018

@author: Samiksha Agarwal
"""

#%%
import pandas as pd
import numpy as np

data=pd.read_csv('F:/2 sem/Foundation/LAB/Naive Bayes Classifier/playtennis2.csv')
# check your datatype
type(data)
#split data into two parts
train=data.drop("day",axis=1)
test = train.iloc[:-5,:]

#%% calculating the probability for class=(yes , no)
'''
        probability(class) =    How many  times it appears in cloumn
                             __________________________________________
                                  count of all class attribute
'''
len_yes=train[train['playtennis']=="yes"].shape[0]
len_no=train[train['playtennis']=="no"].shape[0]
prob_yes=train[train['playtennis']=="yes"].shape[0]/train.shape[0]
prob_no=train[train['playtennis']=="no"].shape[0]/train.shape[0]


column=list(train.columns.values)
#%%
#%% calculate probability for each attribute =(x/yes and x/no)
'''
        Here we calculate the individual probabilites 
        P(outcome|evidence) =   P(Likelihood of Evidence) x Prior prob of outcome
                               ___________________________________________
                                                    P(Evidence)
'''
b=train["playtennis"]=="yes"
c=train["playtennis"]=="no"
df1 = train.iloc[:,:-1]
column=list(df1.columns.values)
probability = {}

for i in column:
    aa={}
    for j in train[i].unique():
        a=train[i]==j
        d=train[a & b].shape[0]
        e=train[a & c].shape[0]
        yes=d/len_yes
        no=e/len_no
        aa[j]={'Yes' : yes,'No': no}
    probability[i]=aa
print()
print('Probability for each attribute =(x/yes and x/no) is -> \n ----------------------------\n',
      probability,'\n','---------------------------')
print('Like an example : probabiltiy for attribute outlook = overcast/yes',probability['outlook']['overcast']['Yes'])
# sunny, high, weak
#%% calculate probability for an attribute
probs1 = {}
for i in column:
    aa={}
    for j in train[i].unique():
        a=train[train[i]==j].shape[0]
        probabilty=a/len(train)
        aa[j]=probabilty
    probs1[i]=aa 
print('Probability for each attribute  is -> \n ----------------------------\n',
      probs1,'\n','---------------------------')  
#%%

gain=(probs1["outlook"]["sunny"]) * (probability["outlook"]["sunny"]["Yes"])

