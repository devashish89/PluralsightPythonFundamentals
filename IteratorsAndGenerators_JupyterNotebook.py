#!/usr/bin/env python
# coding: utf-8

# # Iterators - maintain state

# In[23]:


def fibonacci(num):
    if num<=1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    


# In[24]:


for i in range(10):
    print(fibonacci(i))


# In[25]:


iterator = iter([fibonacci(i) for i in range(30)])


# In[26]:


#Batch1 
counter=0
while counter < 5:
    print(next(iterator))
    counter+=1


# In[27]:


#Batch2
counter=0
while counter < 5:
    print(next(iterator))
    counter+=1


# In[28]:


#Batch3
counter=0
while counter < 5:
    print(next(iterator))
    counter+=1


# # Generators -maintain state like iterators and does not fill the RAM

# In[31]:


def gen_fibonacci():
    a=0
    b=1
    while True:
        f = a+b
        a=b
        b=f
        yield f
        
genObj = gen_fibonacci()


# In[32]:


#Batch1 
for i in range(10):
    print(next(genObj))


# In[33]:


#Batch2
for i in range(10):
    print(next(genObj))


# In[34]:


#Batch3
for i in range(10):
    print(next(genObj))


# In[35]:


#Batch4
for i in range(10):
    print(next(genObj))

