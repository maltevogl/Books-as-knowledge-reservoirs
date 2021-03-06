#!/usr/bin/env python
# coding: utf-8

# # Starting to use Python (and Pandas)

# ## Setup plotting
# 
# To plot data in JupyterLab in a simple fashion use the following code.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# This will display plots directly in the notebook. Note, that there are more advanced displaying options for JupyterLab. The allow for example to zoom in.

# ## Load requiered packages
# 
# Packages offer a wide range of funtionalities, e.g. plotting, calculations, accessing websites with programms. They are mostly listed at [pypi.org](https://pypi.org/) and can be installed either in a terminal or with the [Anaconda](https://www.anaconda.com/distribution/) distribution. 
# 
# Terminal:
# ```bash
# pip install packageName
# ```
# 
# Anaconda:
# > Have a look at the [Cheat Sheet (PDF)](https://docs.anaconda.com/_downloads/9ee215ff15fde24bf01791d719084950/Anaconda-Starter-Guide.pdf)
# 
# For this tutorial, we will need [Pandas](https://pandas.pydata.org/)(Statistics package), [Matplotlib](https://matplotlib.org/)(Plotting package) and [Numpy](https://numpy.org/)(package for numerical work). 

# ## Import package
# 
# After loading the packages, you can access their functionality with the TAB key. If you import the packages like below, the Pandas package e.g. will be available as `pd`. If you add a DOT `pd.`and press the TAB key, you will see a list of possible functions.

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Test the package access. Uncomment and run the cell. You should see a list of methods.

# In[ ]:


#pd.


# ## Create a time series
# 
# Using the Numpy package, we can create a random time series of 1000 entries.

# In[3]:


ts = pd.Series(
  np.random.randn(1000),
  index=pd.date_range('1/1/2020',
  periods=1000)
  )


# ## Create a dataset

# We then create a dataset of random numbers with the time series as an index. Possible columns in the dataset are simply A,B,C and D.

# In[4]:


df = pd.DataFrame(
  np.random.randn(1000, 4),
  index=ts.index,
  columns=['A', 'B', 'C', 'D']
  )


# In[5]:


df.head(2)


# ## Calculate cumulative sum 

# We can calculate the cumulative sum of all columns by running 

# In[6]:


df = df.cumsum()


# Have a look at the beginning of the dataset by simply writing `df.head(5)` and press enter.

# In[7]:


df.head(4)


# ## Plot the dataset
# 
# Since the data is numerical and we have times as index, we can easily create a plot of the dataset by using the `.plot()` method.

# In[8]:


df.plot()


# This is just to give you a small hint on what can be done with Jupyter Notebooks and Phython. In the course of the book, we will introduce many different useful programms and routines to work with text. 

# In[ ]:




