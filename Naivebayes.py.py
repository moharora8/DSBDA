#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import math
import random


# In[2]:


def loadCsv(filename):
    lines=csv.reader(open(r"C:\Users\IAMOHIT\Desktop\pimaindiansdiabetescsv\pima-indians-diabetes.csv"))
    dataset=list(lines)
    for i in range(len(dataset)):
        dataset[i]=[float(x) for x in dataset[i]]
    return dataset


# In[29]:


def splitdataset(dataset,splitratio):
    trainsize=int(len(dataset)*splitratio)
    trainset=[]
    copy=list(dataset)
    while len(trainset)<trainsize:
        index=random.randrange(len(copy))
        trainset.append(copy.pop(index))
    return [trainset,copy]


# In[ ]:





# In[5]:


def seperatedbyclass(dataset):
    seperated={}
    for i in range(len(dataset)):
        vector=dataset[i]
        if(vector[-1] not in seperated):
            seperated[vector[-1]]=[]
        seperated[vector[-1]].append(vector)
    return seperated
        


# In[6]:


def mean(numbers):
    return sum(numbers)/float(len(numbers))


# In[7]:


def stdev(numbers):
    avg=mean(numbers)
    variance=sum([pow(x-avg,2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)


# In[9]:


def summarize(dataset):
    summaries=[(mean(attribute),stdev(attribute)) for attribute in zip(*dataset)]
    del summaries[-1]
    return summaries


# In[11]:


def summarisedbyclass(dataset):
    seperated=seperatedbyclass(dataset)
    summaries={}
    for classValue,instances in seperated.items():
        summaries[classValue]=summarize(instances)
    return summaries


# In[12]:


def calculateprobability(x,mean,stdev):
    exponent=math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1/(math.sqrt(2*math.pi)*stdev))*exponent


# In[33]:


def calculateclassprob(summaries,inputVector):
    probabilities={}
    for classValue,classSummaries in summaries.items():
        probabilities[classValue]=1
        for i in range(len(classSummaries)):
            mean,stdev=classSummaries[i]
            x=inputVector[i]
            probabilities[classValue]*=calculateprobability(x,mean,stdev)
        return probabilities


# In[ ]:





# In[35]:


def predict(summaries,inputVector):
    probabilities=calculateclassprob(summaries,inputVector)
    bestlabel,bestprob=None,-1
    for classValue,probability in probabilities.items():
        if bestlabel is None or probability>bestprob:
            bestprob=probability
            bestlabel=classValue
    return bestlabel


# In[ ]:





# In[31]:


def getpredictions(summaries,testset):
    predictions=[]
    for i in range(len(testset)):
        result=predict(summaries,testset[i])
        predictions.append(result)
    return predictions


# In[ ]:





# In[37]:


def getaccuracy(testset,predictions):
    correct=0
    for x in range(len(testset)):
        if testset[x][-1]==predictions[x]:
            correct+=1
    return (correct/float(len(testset)))*100
        


# In[ ]:





# In[54]:


def main():
    filename="pima-indians-diabetes.csv"
    splitratio=0.67
    dataset=loadCsv(filename)
    trainingset,testset=splitdataset(dataset, splitratio)
    print('split{0} rows into train={1} and test={2} rows'.format(len(dataset),len(trainingset),len(testset)))
    #prepare model
    summaries=summarisedbyclass(trainingset)
    #test model
    predictions=getpredictions(summaries,testset)
    accuracy=getaccuracy(testset,predictions)
    print('Accuracy:{0}%'.format(accuracy))
main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[25]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




