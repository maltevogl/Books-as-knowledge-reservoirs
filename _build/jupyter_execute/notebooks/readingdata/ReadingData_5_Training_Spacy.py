#!/usr/bin/env python
# coding: utf-8

# # Training a new spacy model for Tucholsky
# 
# Spacy offers a relativly simple training pipeline. It uses an exisiting model and introduces new categories to this model.
# 
# As always with ml methods, the question is how to get training data. In this exercise, a simple method using regular expressions is shown. 
# More useful results however, are obtained using a manually tagged input e.g. from Doccano. 

# In[ ]:


import spacy
import random
import numpy as np
from spacy.pipeline import EntityRecognizer


# In[ ]:


import pandas as pd
import re
from itertools import tee


# In[ ]:


df_all = pd.read_json('PATH_TO/df_tucholsky.json',lines=True)


# For simplicity and speed we limit ourselfs to those texts containing the word 'Krieg' (german for _War_).

# In[ ]:


df = df_all[df_all.text.str.contains('\sKrieg\s')]


# ## Create labels by regular expressions
# 
# Using regular expressions, we create three new labels, the name of the publication, the publishing data, and the pseudonym used. These are all simple tags, since their occurance is either very formalized (e.g. the publication name is always followed by date) or limited (the number of used pseudonyms).

# In[ ]:


def getValue(text):
    regex = [('Publication Name','(?<=\n).+(?=,\s\d{2}.\d{2}.\d{4})'), ('Date','\d{2}.\d{2}.\d{4}'), ('Pseudonym','Kaspar Hauser|Ignaz Wrobel|Kurt Tucholsky|Paul Panther|Theobald Tiger')]
    retList = []
    for exp in regex:
        expr = re.compile(exp[1])
        try:
            find = re.search(expr, text)
            retList.append([find.start(), find.end(), exp[0]])
        except AttributeError:
            pass
    return retList


# Testing the routing before its application on the full dataframe is a good practice.

# In[ ]:


getValue(df.text.iloc[0])


# We create a new column called labels, which contains the results of the routine.

# In[ ]:


df['labels'] = df.text.apply(lambda row: getValue(row))


# Test the output of the routine by looking at the head of the dataframe.

# In[ ]:


df.head(2)


# ## Training part

# To create training data we have to use the correct format for Spacy. Each text is saved with its found entities in a tuple and added to a list.

# In[ ]:


TRAIN_DATA = []


# In[ ]:


for row in df.iterrows():
    TRAIN_DATA.append((row[1]['text'],{'entities':row[1]['labels']}))


# We can now take the part of the Spacy pipeline we want to train (Named Entity Recognition, NER), and add the new labels.

# In[ ]:


nlp = spacy.load("de_core_news_md")
ner = nlp.get_pipe('ner')
ner.add_label("Pseudonym")
ner.add_label("Publication Name")
ner.add_label("Date")


# The training itself is started using the following syntax. Note, that it is limited to 20 texts to keep the runtime short.

# In[ ]:


optimizer = nlp.begin_training()
for i in range(20):
    random.shuffle(TRAIN_DATA)
    for text, annotations in TRAIN_DATA:
        nlp.update([text], [annotations], sgd=optimizer)


# The resulting newly trained model can be saved to disk for later use. Uncomment the following cell to save the model.

# In[ ]:


#nlp.to_disk("../data/tucholsky.model")


# ## Using pre-tagged data
# 
# To use a pre-tagged dataset for tagging (in the Docanno format) we only need to make slight adaptions of the procedure. The example dataset has more new labels.

# In[ ]:


data = pd.read_json('../data/DocannoCorpus.json',lines=True)


# In[ ]:


data.head(2)


# In[ ]:


TRAIN_DATA = []


# In[ ]:


for row in data.iterrows():
    if row[1]['labels']:
        TRAIN_DATA.append((row[1]['text'],{'entities':row[1]['labels']}))


# In[ ]:


l = np.array(TRAIN_DATA)[:,1]


# In[ ]:


l[0]


# In[ ]:


nlp_doc = spacy.load("de_core_news_md")


# In[ ]:


ner = nlp_doc.get_pipe('ner')
ner.add_label("Pseudonym")
ner.add_label("Publication name")
ner.add_label("Date")
ner.add_label("Title of piece of art")
ner.add_label("Location")
ner.add_label("Person (real)")
ner.add_label("Organization")
ner.add_label("Person (fictional)")


optimizer = nlp_doc.begin_training()
for i in range(20):
    random.shuffle(TRAIN_DATA)
    for text, annotations in TRAIN_DATA:
        nlp_doc.update([text], [annotations], sgd=optimizer)


# In[ ]:


#nlp_doc.to_disk("../data/tucholsky_doccano.model")


# ### Exercise
# 
# Use the previous notebook that introduced Spacy and load one of the newly trained models for Tucholsky. 
# 
#   - Do you see any difference in the routines of Spacy?
#   - Use the displacy method for visualizing entities! 

# In[ ]:




