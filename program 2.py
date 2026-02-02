#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
np.__version__


# In[11]:


#Arrays
arr  = np.array([1,2,3,4,5])
print (arr)
print(type(arr))
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)


# In[16]:


#Reshaping arrays
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new = arr.reshape(4,3)
print(new)
neww = arr.reshape(2,3,2)
print(neww)


# In[17]:


np.zeros(10,dtype = 'int')


# In[25]:


a = np.ones(10, dtype = 'int')
b = np.ones(10, dtype = 'float')
print(a)
print(b)


# In[21]:


np.full((3,5),1.23)


# In[23]:


np.arange(0,20,2)


# In[27]:


arr = np.array([1,2,3,4,5])
for x in arr:
    print(x)


# In[32]:


arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    for y in x : 
        print(y)


# In[33]:


np.random.normal(0,1,(3,3))


# In[34]:


np.eye(3)


# In[39]:


np.random.seed(0)
x1 = np.random.randint(10, size = 6)
x2 = np.random.randint(10, size = (3,4))
x3 = np.random.randint(10, size = (3,4,5))
print(x1)
print(x2)
print(x3)


# In[43]:


arr1 = np.array([[1,2,3]])
arr2 = np.array([[4,5,6]])
new = np.concatenate((arr1,arr2))
print(new)


# In[44]:


#Indexing and Slicing
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[0])


# In[46]:


print(arr[:6])


# In[47]:


print(arr[4:])


# In[48]:


print(arr[3:7])


# In[51]:


print(arr[:-1])


# In[52]:


print(arr[1:5:2])


# In[54]:


#reverse the array
arr[::-1]


# In[55]:


import pandas as pd
pd.__version__


# In[56]:


#Series
a = [1,2,3,4,5]
s = pd.Series(a)
print(s)


# In[57]:


#Labels
print(s[0])


# In[59]:


a = [1,2,3]
s = pd.Series(a, index = ['x','y','z'])
print(s)


# In[61]:


print(s["y"])


# In[ ]:




