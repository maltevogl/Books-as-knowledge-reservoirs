#!/usr/bin/env python
# coding: utf-8

# # Using Spacy for POS tagging
# 
# Many NLP tools use machine learning in the backend. This is the case for NLTK and also for Grobid, the tool that converted OCR text to TEI. [Delft](https://github.com/kermitt2/delft) is the ml framework behind Grobid and it uses pre-trainend _word embeddings_ (later!) to create models for tagging and other tasks. Tagged data from external sources e.g. using the Doccano software, can be used to train a _Tucholsky tagger_.
# 
# ## Some ML basics
# 
# For training a ml model, we need (large) datasets. Usually a dataset is split in 80/20 % sets, where 80%  are used for training and 20% for testing the resulting model. During this _"learning"_ procedure the f1 score is used to monitor progress. It describes the mean of precision and recall, where _precision_ is the number of correct positives vs all returned positives and _recall_ is the number of correct positives vs all possible correct positives. This is a similar concept as the so called _confusion matrix_. 
# 
# ## What is Spacy ? 
# 
# [Spacy](https://spacy.io) is slighlty more modern than NLTK. It includes pre-trained models for other languages then english (e.g. [German](https://spacy.io/models/de)) and has lots of functionality to interlink with other Python AI software. Another nice thing are the in-build functions for visualization.What

# ## Using Spacy
# 
# As previously, there is a cell to be edited!

# In[ ]:


import spacy
from spacy import displacy
import pandas as pd


# In[ ]:


data = pd.read_json('../data/df_tucholsky.json', lines=True)


# Sort entries by publishing date.

# In[ ]:


data = data.sort_values('year') 


# In[ ]:


data.head(4)


# The spacy model has to be loaded depending on the language. For Tucholsky we try _de_core_news_md_, which is a medium sized model, trained on two german corpora.
# 
#   - Tiger corpus: https://www.ims.uni-stuttgart.de/forschung/ressourcen/korpora/tiger/
#   - WikiNER: https://figshare.com/articles/Learning_multilingual_named_entity_recognition_from_Wikipedia/5462500
#   
# Note, that both are trained on modern german language!
# 
# This might take some time, up to a minute or more.
# 
# To download the language model, remove the hash from the following cell. Sometimes, the kernel needs to be restarted after you have finished downloading the model.

# In[ ]:


# ! python -m spacy download de_core_news_sm


# In[ ]:


nlp = spacy.load("de_core_news_sm")


# In Spacy all characteristics of a text are represented in `doc` models. By default, a large number of these are created in _spacy pipelines_ automatically. We can create such a doc instance by passing the text into the `nlp` instance.
# 
#   - Chose a text by accessing a row number in the text column
#   - Use a small text to speed-up calculation time

# In[ ]:


text = data.text.iloc[???]
len(text)


# In[ ]:


doc = nlp(text)


# A document contains the text and its tokens. Tokens have different sub-methods to access e.g. the lemma, the POS tag or recognized entities. 

# We first access the token tags by using

# In[ ]:


for token in doc[:20]:
    print(token.text, token.lemma_, token.pos_, token.tag_)


# A build-in visualization functions `displacy.render()` allows for example to display the relations between the tokens. Note, that such plots are build for single sentences and become quite large.

# In[ ]:


displacy.render(doc[:20], style="dep")


# The loaded german model is only capable of tagging a small set of entities (_Persons_, _Locations_, _Organizations_, and _Misc_). These entites can be accessed as follows

# In[ ]:


for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)


# Similar to the Doccano format, results for entities contain the text, start and stop character and the label. Using the visualization capabilities gives a similar picture to the Doccano tagging. As visible, the accuracy is pretty low. Similar excercises for english texts give much better results, since there are models available trained on much larger corpora.

# In[ ]:


displacy.render(doc, style="ent")


# In[ ]:




