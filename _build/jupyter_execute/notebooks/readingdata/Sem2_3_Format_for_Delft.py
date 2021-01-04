# Export format from Doccano to Delft 

The annotated texts from Doccano have to be re-formated to be readable by Delft, a machine-learning library for finding and annotating text parts.

import pandas as pd
from itertools import tee

data = pd.read_json('/home/mvogl/Downloads/file(3).json1',lines=True)

data.head()

Each annotation set has the form (start,stop,tag). In principle this allows to easily re-format. However, changing one text shifts all word boundaries. We therefore have to create a list of all tagged words and the text in between them. Tagged words are re-formated and in the end of the routine, the new re-formated text is joined together. 

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def formatDelft(row):
    text = row['text']
    
    textParts = []
    if not row['labels']:
        return ''
    for elem in pairwise(sorted(row['labels'])):
        if elem[0][0] != 0:
            textParts.append([0,elem[0][0],'text'])
        textParts.append(elem[0])
        textParts.append([elem[0][1],elem[1][0],'text'])
    if textParts[-1][1] != len(text):
        textParts.append([textParts[-1][1],len(text),'text'])
        
    formatedParts = []
    
    for elem in textParts:
        textelem = text[elem[0]:elem[1]]
        if elem[2] != 'text':
            subtext = '<rs type="{0}">{1}</rs>'.format(elem[2],textelem)
        else:
            subtext = textelem
        formatedParts.append(subtext)
        
    return ''.join(formatedParts) #3

data['delftFormated'] = data.apply(lambda row: formatDelft(row),axis=1)

data[data['delftFormated'] != ''].delftFormated.iloc[0]

startTEI = """
<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns:mml="http://www.w3.org/1998/Math/MathML" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.tei-c.org/ns/1.0">
"""
endTEI = "</TEI>"

with open('./data/delft_test.xml','a+') as file:
    file.write(startTEI)
    for line in data.delftFormated.unique():
        if line:
            file.write("<p>{0}</p>".format(line))
    file.write(endTEI)
    

