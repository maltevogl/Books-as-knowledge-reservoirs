#!/usr/bin/env python
# coding: utf-8

# # Read all works by Tucholsky
# 
# The basic dataset for the book will be a collection of all works by Tucholsky. The reason for this is simply that building a clean research corpus is a difficult and long processes in itself, deeply connected to your research question. For the aim of this book, it is therefore easier to focus on an already existing corpus. 

# ## Reading TEI file
# 
# Textual corpora are mostly encoded in TEI XML format. Collected works of Kurt Tucholsky can for example be found in the [TextGrid](https://textgrid.de/digitale-bibliothek) repository.
# 
# Source:
# 
#   >  TextGrid Repository (2012). Tucholsky, Kurt. Werke. Digitale Bibliothek. TextGrid. https://hdl.handle.net/11858/00-1734-0000-0005-61C5-B 

# In[1]:


import os
import re
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
import pandas as pd
from bs4 import BeautifulSoup
import xml.etree.ElementTree as etree


# In[2]:


fileList = os.listdir('../data/tei/')


# ### Reducing the structure
# 
# Since we are not concerned with the finer textual structure, we simple read the full text of every identified text.
# 
# First, we look at XML elements of the form _./tei:teiCorpus/tei:TEI_ and extract the title and publication year. 
# Then, we open the file with BeatifulSoup to find _div_ elements which have the correct _textID_ and collect the full text from them. 
# 
# The resulting list contains all texts by Tucholsky which are available in this resource, their titles and publication years. 
# Overall, we have around 1700 texts between 1917 and 1934.

# In[3]:


def getText(path):
    ##
    ns = {'tei':"http://www.tei-c.org/ns/1.0","xml":"http://www.w3.org/XML/1998/namespace"}
    dateRegex = re.compile('(?<=/Literatur/M/Tucholsky, Kurt/Werke/)\d{4}(?=/)')
    titleRegex = re.compile('(?<=/Literatur/M/Tucholsky, Kurt/Werke/\d{4}/).+')
    basePath = '../data/tei/'
    ###
    filePath = basePath + path
    tempList = []
    if os.path.isfile(filePath) and path.endswith('.xml'):
        tree = etree.parse(filePath)
        root = tree.getroot()
        TEIs = root.findall("./tei:teiCorpus/tei:TEI",ns)
        for el in TEIs:
            tempDict = {}
            tempDict['ids'] = el.attrib["{http://www.w3.org/XML/1998/namespace}id"]
            tei_path = el.attrib['n']
            tempDict['year'] = int(re.findall(dateRegex,tei_path)[0])
            tempDict['title'] =  re.findall(titleRegex,tei_path)[0]
            tempList.append(tempDict)
        with open(filePath) as file:
            soup = BeautifulSoup(file,'lxml')
            for ids in tempList:
                try:
                    search = re.compile(ids['ids'].split('.')[0] + '+')
                    elems = soup.findAll('div',{'xml:id':search})
                    assert len(elems) == 1
                    text = elems[0].getText()
                    ids.update({'text':text})
                except:
                    print(ids)
                    search = re.compile(ids['title'] + '+')
                    elems = soup.findAll('div',{'n':search})
                    textList = [x.getText() for x in elems]
                    text = '\n\n\n\n'.join(textList)
                    ids.update({'text':text})
                    print('Found text for ids')
    return tempList


# In[4]:


pool = Pool(cpu_count() - 1)


# In[5]:


result = pool.map(getText,fileList)


# In[6]:


flatt = [x for y in result for x in y]


# In[8]:


dfT = pd.DataFrame(flatt)
dfT.head(2)


# We can easily check that all ids have a corresponding text.

# In[ ]:


dfT[dfT.text.isna()]


# The resulting dataframe is saved in JSONL format for further processing.

# In[10]:


dfT.to_json('../data/df_tucholsky.json', orient='records', lines=True)


# In[ ]:




