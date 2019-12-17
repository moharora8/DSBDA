#!/usr/bin/env python
# coding: utf-8

# In[51]:
#Not yet finished

import csv
with open('C:\Users\IAMOHIT\Desktop\habermans-survival-data-set\Iris.csv','rb') as csvfile:
    lines=csv.reader(csvfile)
    for row in lines:
        print ', '.join(row)


# In[ ]:





# In[ ]:





# In[ ]:





# In[55]:


import csv
import random
def loadDataset(filename,split,trainingset=[],testset=[]):
    with open('C:\Users\IAMOHIT\Desktop\habermans-survival-data-set\Iris.csv','r') as csvfile:
        lines=csv.reader(csvfile)
        dataset=list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y]=float(dataset[x][y])
            if random.random()<split:
                trainingset.append(dataset[x])
            else:
                testset.append(dataset[x])
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[58]:


trainingset=[]
testset=[]
loadDataset('C:\Users\IAMOHIT\Desktop\habermans-survival-data-set\Iris.csv',0.66,trainingset,testset)
print('Train: '+repr(len(trainingset)))
print('Test: '+repr(len(testset)))


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





# In[17]:


import math
def eucledian(instance1,instance2,length):
    distance=0
    for x in range(length):
        distance+=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)


# In[20]:


data1=[2,2,2,'a']
data2=[4,4,4,'b']
distance=eucledian(data1,data2,3)
print 'Distance: '+repr(distance)


# In[29]:


import operator
def getneighbours(trainingset,testinstance,k):
    distances=[]
    length=len(testinstance)-1
    for x in range(len(trainingset)):
        dist=eucledian(testinstance,trainingset[x],length)
        distances.append((trainingset[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


# In[ ]:





# In[ ]:





# In[ ]:





# In[30]:


trainset=[[2,2,2,'a'],[4,4,4,'b']]
testinstance=[5,5,5]
k=1
neighbors=getneighbours(trainset,testinstance,1)
print(neighbors)


# In[31]:


import operator
def getresponse(neighbors):
    classvotes={}
    for x in range(len(neighbors)):
        response=neighbors[x][-1]
        if response in classvotes:
            classvotes[response]+=1
        else:
            classvotes[response]=1
    sortedvotes=sorted(classvotes.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedvotes[0][0]
    


# In[32]:


neighbors=[[1,1,1,'a'],[2,2,2,'a'],[3,3,3,'b']]
response=getresponse(neighbors)
print(response)


# In[34]:


def getaccuracy(testset,predictions):
    correct=0
    for x in range(len(testset)):
        if testset[x][-1] is predictions[x]:
            correct+=1
    return (correct/float(len(testset)))*100.0


# In[38]:


# testset=[[1,1,1,'a'],[2,2,2,'a'],[3,3,3,'b']]
# predictions=['a','a','a']
# accuracy=getaccuracy(testset,predictions)
# print(accuracy)


# In[39]:


def main():
    #prepare data
    trainingset=[]
    testset=[]
    split=0.67
    loadDataset('iris.data',split,trainingset,testset)
    print 'Train set:'+repr(len(trainingset))
    print 'Test set:'+repr(len(testset))
    #generate predictions
    predictions=[]
    k=3
    for x in range(len(testset)):
        neighbors=getneighbours(trainingset,testset[x],k)
        result=getresponse(neighbors)
        predictions.append(result)
        print('>predicted='+repr(result)+'actual='+repr(testset[x][-1]))
    accuracy=getaccuracy(testset,predictions)
    print('Accuracy:' +repr(accuracy)+'%')
    
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




