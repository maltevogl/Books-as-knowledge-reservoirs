#!/usr/bin/env python
# coding: utf-8

# # Load JSONL with pandas
# This notebook is purposfully not ready to be evaluated! You need to read and check every code and text cell and fill in some missing pieces. Mostly, they are marked by three question marks (???).
# 
# At the end, there is a bonus question with a slightly more involved exercise.
# 
# ## Read file into pandas
# 
# Enter the path to your downloaded corpus file.

# In[ ]:


import pandas as pd


# In[ ]:


data = pd.read_json('../data/df_tucholsky.json', lines=True)


# The read-in file is now assigned to the variable `data`.

# In[ ]:


data.head()


# The size of the dataframe (i.e. table) can be obtained by using

# In[ ]:


data.shape


# The first number gives the number of rows, the second the number of columns. 

# ## Check structure and access data

# You can access a column by using the column name, e.g. `data['name']`.

# In[ ]:


data['ids']


# To read a specific row, you can use the function `.iloc[NUMBER]` to access by count, or select a specific row by content. 
# This happens in two steps.
# First, you create a list of True/False values, and then reduce the data to rows which are True. 

# To create a _boolean mask_ (True/False list) for numbers you can use _comparision operators_, i.e. `==` for equal, or `>=` for greater then. 
# 
# Example: `data['COLUMN'] >= 10` or `data['COLUMN'] == 17`
# 
# You can combine several conditions by using AND (`&`, `and`) and OR (`|`, `or`)  operators, e.g. `cond=(cond1 & cond2)`, .
# 
# Example:  `data[(cond1 & cond2)]`
# 
#   - Select all rows of the year 1911
#   - BONUS: Select all rows for the years 1920 to 1925

# In[ ]:


yearMask1 = data.year == ???


# In[ ]:


data[yearMask1]


# In[ ]:


yearMask2 = (data.year >=1920) & ???


# In[ ]:


data[yearMask2].head(2)


# To select rows which contain text, we can use _string comparision_. For accessing all rows, which contain the text `hello`, we create a mask `cond = data["COLUMN"].str.contains("hello")` and apply it to the data as above. 
# 
#   - Select all rows, where the title contains the word _Krieg_, (German for _war_)
#   - BONUS: Select all rows where the title contains _Krieg_, which are published before 1924

# In[ ]:


text = 'test string'


# In[ ]:


['test' in text]


# In[ ]:


textMask = data.text.str.contains(???)


# In[ ]:


data[textMask]


# To test whether the text is correctly found, we can simply read the full text of a found work.

# In[ ]:


data[textMask].text.iloc[2]


# ## Sort data by publication years
# 
# To group a dataset by a certain column, we can use pandas `.groupby` function. It returns a _generator_-like object containing tuples of sub-dataframes with the value of the grouped column, e.g. `1911,data_for_1911)`.
# 
# To get a specific group, you can use `.get_group(VALUE)` on the resulting grouped object.  

# In[ ]:


grouped = data.groupby('year')


#  - Select the group for the year 1917

# In[ ]:


grouped.get_group(???)


# For the size of each group (i.e. number of rows) we have the function `.size()`.
#   - Get a list of sizes for each year group

# In[ ]:


grouped.???


# ## Plot resulting dataset
# 
# Sometimes a plot gives a good overview over a dataset.
# 
# For dataframes containing only numbers, its easy to generate graphs with pandas build-in functions `.plot()`. Bar charts can be obtained with `.plot.bar()`.

#   - Generate a plot of the number of publications per year

#  - Bonus: Generate a plot of the number of publications, which where published with the different pseudonyms of Tucholsky ('Wrobel', 'Hauser', 'Tiger', 'Panter') and compare them to the overall publication output and the publications published under his real name. Can you normalize the data for each year? 

# In[ ]:




