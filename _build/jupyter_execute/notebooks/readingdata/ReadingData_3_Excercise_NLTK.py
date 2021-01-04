#!/usr/bin/env python
# coding: utf-8

# # Working with NLTK
# 
# As previously, cells need to be completed where marked with ??? and there is a bonus question at the end.
# 
# This excercise gives a short introduction to the package `nltk`, which is described in full-length in the website [nltk.org/book](http://www.nltk.org/book).

# In[ ]:


import nltk
from nltk import word_tokenize, FreqDist
import pandas as pd
import matplotlib.pylab as plt


# If you get package errors, that data is missing, you can use `nltk.download()` to get them.

# In[ ]:


#nltk.download('punkt')


# In[ ]:


data = pd.read_json('../data/df_tucholsky.json', lines=True)


# Sort data by publication year

# In[ ]:


data = data.sort_values('year')


# Select subset of texts containing
# "Krieg" as a separate word.

# In[ ]:


subset = data[data.text.str.contains('\sKrieg\s')]


# We have around 200 texts.

# In[ ]:


subset.shape


# Create a list of transformed texts and word frequencies.

# In[ ]:


allTexts = [] 
for i,row in subset.iterrows():
    name = "{0} ({1})".format(row['title'],row['year'])
    tokens = word_tokenize(row['text'])
    text = nltk.Text(tokens,name)
    fdist = FreqDist(text)
    allTexts.append([text, fdist])


# Lets have a look at one specific text. Since the list `allTexts`contains elements of lists we can define the values for text and frequency distribution as follows

# In[ ]:


text5, fdist5 = allTexts[5]


# Running the code cell with only the `text5` variable, will print the title and year.

# In[ ]:


len(text5.tokens)


# Test the `concordance(WORD)` and other functions with some words
#   - Concordance of "Krieg", "Politik", "Ethik"
#   - Similar of "Politik"
#   - Common context of "Politik" and "Ethik"

# In[ ]:


text5.concordance(???)


# We can check which words have a similar context by using `similar(WORD)`

# In[ ]:


text5.similar(???)


# Related to the `similar()` function, we can check for `common_contexts([WORD1, WORD2])`.

# In[ ]:


text5.common_contexts([???,???])


# The function `collocations()` gives groups of words that often occure together.

# In[ ]:


text5.collocations()


# To quickly visualize the occurance of words throughout a text, we can use `dispersion_plot([WORD1, WORD2])`.
# 
#   - Plot the dispersion of "Krieg", "Politik" and "Ethik"

# In[ ]:


text5.dispersion_plot([???,???,???])


# ## Frequency distributions
# 
# Frequency distributions describe the number of occurances of words in a text. To find the most common words use `most_common`. This returns a ordered list of words and their occurance in the text. 

# In[ ]:


fdist5.most_common(20)


# Inputing a specific word gives the number of occurances.
# 
#   - Check for "Krieg" and "Politik"

# In[ ]:


fdist5[???]


# To find the opposite end, i.e. words which occure only once, we can use `.hapaxes()`. _Hapax legomenon_ are sometimes used to characterize the unknown authors of texts. 
# 
#   - Are they a useful candidate for _keywords_ to describe the character of a document? 
#   - why? Why not? 

# In[ ]:


fdist5.hapaxes()[:20]


# Another option for keywords could be a mix of often occuring and long enough words.
# 
#   - In the following code, find a combination of length and frequency that gives useful words

# In[ ]:


length = 5
frequency = 4
sorted(w for w in set(text5) if len(w) > length and fdist5[w] > frequency)


# Fdist also offers plotting, e.g. to see how the most common words shape the whole text.

# In[ ]:


fdist5.plot(50, cumulative=True)


# In[ ]:


print(fdist5)


# Since there are only around 1200 words in the text, the 50 most common words are building 50 % of the text.

# ## Bonus: Zipf's law
# 
# [Zipf's law](https://en.wikipedia.org/wiki/Zipf%27s_law) is claimed to be a general law in language, that in any natural language text the frequency of every word is inverse to its rank in the frequency table. This means, that if you order all words of a text by their occurance, and give them a number related to their position in the ordered list, a log-log plot of (rank,frequency) should be linear. 
# 
#   - Bonus: Reproduce Zipf's law for a given Tucholsky text
#   - Hints: 
#     - Use matplotlib [scatter plot](https://pythonspot.com/matplotlib-scatterplot/)
#     - 'fdist.B' gives the number of bins, i.e. words in a corpus, same as len(fdist)
#     - How do you get all the first elements in a list of lists?
#     - plt.xscale('log) and plt.yscale('log') set logarithmic scales
#   - Bonus II: Write a function returning the plot for any input text, with the text title as plot title
#   - Hints: 
#     - plt.title(text) sets the title of a plot

# In[ ]:


#def plot(text):
#
#    return p


# In[ ]:


#plot(allTexts[10])


# In[ ]:




