#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Function takes a list and uses a loop to print the given message that pizza is ready
def waiting(customers):
    """ Sends a message to all waiting customers """

    for name in customers:
        print("Your pizza is almost ready",name.title())

customers = ['Chan','Felix','Jake','Kai','Terry','Jay']

waiting(customers)


# In[ ]:




