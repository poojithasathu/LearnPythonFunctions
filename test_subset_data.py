#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#Read csv file
df_raw = pd.read_csv('C:/Users/LENOVO/Documents/Data1202/vgsales.csv')


# In[3]:


# Build a function to subset the data using iloc function
def subset_data(df_raw, row_select, col_select):
  # DOCSTRING
  """
  This function is used to dynamically slice data from 
  a users dataframe. 

  row_select: this represents the rows the user wants
  col_select: this is the columns
  """
  #Slicing the dataframe using iloc function  
  subset = df_raw.iloc[row_select, col_select]
  
  #return this value
  return subset


# In[4]:


#call the function using different input 
first_row = subset_data(df_raw, 0, [0,1,2,3])
tenth_row = subset_data(df_raw, 10, [0, 1, 2, 3])

print(first_row)
print(tenth_row)


# In[ ]:




