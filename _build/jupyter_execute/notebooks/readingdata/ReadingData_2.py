#!/usr/bin/env python
# coding: utf-8

# # Finding and counting words
# 
# As allways some cells need to be edited to run this exercise. Mostly, these parts are marked by ???.
# 
# As in the previous excercise, first load the data from the saved file.

# In[ ]:


import re
import pandas as pd


# In[ ]:


data = pd.read_json('../data/df_tucholsky.json',lines=True)


# For counting the number of words in each text, we can use different methods. 
# 
# For example, every text variable in Python has functionalities to work with it, e.g. `.split()`, .`strip()`, .`startswith()`

# We can text some functionalities by taking the first text from the dataframe.

# In[ ]:


data.head(2)


# In[ ]:


text = data['text'].iloc[0]


# The text itself is returned by printing the current variable value

# In[ ]:


text


# If you want to have the text correctly formated, you need to `print()` it!

# In[ ]:


print(text)


# If we apply `.strip()` we remove whitespaces and newlines at the beginning and end of the text.

# In[ ]:


newtext = text.strip()
newtext


# The new text starts with the word _Der_ which can be checked with the function `.startswith()`.

# In[ ]:


newtext.startswith('Der')


#   - Try to use `.endswith('WORD')` on the variable _newtext_, such that the function returns True. 
# 

# In[ ]:


newtext.endswith(???)


# ## Counting words

# If we apply the function `.split()` the text will be split at each whitespace, which is the default. You can also apply any string value and the text will be split for example at each letter _e_ (`.split('e'))`

# In[ ]:


splitted = newtext.split()


# The return value of splitting is a list of the splitted elements. To get the number of list elements, you can use the `len()` command. 

# In[ ]:


len(splitted)


#   - What happens if you split the text on newline characters? (`"\n"`) 

# Splitting at whitespaces is almost a word list of the text, but there are some symbols like hyphens and words are followed by dots or so.

# In[ ]:


splitted


# ### with Regular expressions 

# If we build a wordlist or count based on this list, we will get wrong results. A slightly better way is using __regular expressions__, a formal way to talk about language.

# The Python package `re` imported in the first line, is dealing with regular expressions.
# 
# To find regular expressions, we use `re.findall(EXPRESSION, TEXT)`.

# The expression `[A-Z]` matches all capital letter. Adding a plus `[A-Z]+` matches strings of one or more capital letters. If you want to match a certain number of capital letters, you can add curly brackets with the needed numbers `{2,4}` (between two and four), `{3}` (exactly three) or `{2,}` (two or more).

#  - Use regular expressions to find all capital letters
#  - Are there also two capital letters together? 
#  - Use the parameter `\d` to find exactly four digits. What number is this?
#  - BONUS: Find an expression to match a date? (e.g. 12.06.2020)
#  - BONUS: Can you create an expression to find the publishing metadata of `Die Weltbühne` (which issue, page)? 

# Combining capital and small letters with a plus finds a number of word-like objects, but some special characters of German are lost (e.g. _ß_). As a shortcut, one can use `\w` to find all alpha-numeric characters.

# In[ ]:


#re.findall('[A-Z]..\s[A-z]',text)


# To find the number of all words in every text, we need to write a small function in Python.
# 
# A function always has the form 
# 
# ```python
# def NAME(INPUT):
#     var = FUNCTION(INPUT)
#     return var
# ```
# 
# In our case, the input is a text and the returned variable should be the length of the list of words.
# 
#   - Write the function with `re.findall()`, the input variable _text_ and outputing the len of the word list

# In[ ]:


def wordNumber(text):
    var = len(re.findall(???,text))
    return var


# The new function can be applied to the data by using the `.apply()` function of dataframes.

# In[ ]:


newdata = data.text.apply(lambda x: wordNumber(x))


# This automatically applies the function to every row of the dataframe. To save the information in the dataframe, create a new column.

# In[ ]:


data['wordCount'] = newdata 


# If you want to check you result, uncomment the cell below (i.e. remove the hash sign).

# In[ ]:


#data.wordCount


# ## Count unique words

# To get an overview of the used words in each text, we can use the `Counter` function from the in-built _collections_ package

# In[ ]:


from collections import Counter


# Counting the words of one text is simply done by

# In[ ]:


allwords = re.findall('\w+',text)
Counter(allwords)


#   - Write a function to return the list of counted words for each text.
#   - Bonus: Try to _normalize_ the counts by the number of words in the text. 
#   - Bonus: Return the counted words ordered by the highest count. _Hint_: Try the most_common() method of the returned Counter object.

# ## Plotting the output of Tucholsky
# 
# Using the plotting functionality of Pandas introduced in Excercise 1, we can create an overview of Tucholsky's "productivity" over the years.
# 
#   - Frist, create a sub-dataframe by selecting the columns for year and wordcount by making a list of the column names `cols = ["year","wordCount"]`
#   - Second, group the sub-dataframe by the `year` column
#   - Third, calculate the `.mean()`
#   - Then, plot the yearly as a bar graph by using `.plot.bar()`
#   

# Define the columns

# In[ ]:


#cols =


# Select the sub-dataframe.

# In[ ]:


#subdata = data[cols]


# Group the dataframe by years

# In[ ]:


#grouped = 


# Calculate the mean number of words for each year

# In[ ]:


#mean = grouped


# Plot the data as a bar graph

# In[ ]:


#mean


# ## Save extended data to new file

# In[ ]:


#data.to_json('PATH_TO_NEW_FILE','tucholsky_meta')


# In[ ]:




