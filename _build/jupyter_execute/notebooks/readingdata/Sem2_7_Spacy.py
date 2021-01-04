# Using Spacy for POS tagging

import spacy
from spacy import displacy
import pandas as pd

data = pd.read_hdf('PATH_TO_TUCHOLSKY_META')

Sort entries by publishing date.

data = data.sort_values('year') 

data.head(4)

The spacy model has to be loaded depending on the language. For Tucholsky we try _de_core_news_md_, which is a medium sized model, trained on two german corpora.

  - Tiger corpus: https://www.ims.uni-stuttgart.de/forschung/ressourcen/korpora/tiger/
  - WikiNER: https://figshare.com/articles/Learning_multilingual_named_entity_recognition_from_Wikipedia/5462500
  
Note, that both are trained on modern german language!

This might take some time, up to a minute or more.

nlp = spacy.load("de_core_news_md")

In Spacy all characteristics of a text are represented in `doc` models. By default, a large number of these are created in _spacy pipelines_ automatically. We can create such a doc instance by passing the text into the `nlp` instance.

  - Chose a text by accessing a row number in the text column
  - Use a small text to speed-up calculation time

text = data.text.iloc['NUMBER']
len(text)

doc = nlp(text)

A document contains the text and its tokens. Tokens have different sub-methods to access e.g. the lemma, the POS tag or recognized entities. 

We first access the token tags by using

for token in doc[:20]:
    print(token.text, token.lemma_, token.pos_, token.tag_)

A build-in visualization functions `displacy.render()` allows for example to display the relations between the tokens. Note, that such plots are build for single sentences and become quite large.

displacy.render(doc[:20], style="dep")

The loaded german model is only capable of tagging a small set of entities (_Persons_, _Locations_, _Organizations_, and _Misc_). These entites can be accessed as follows

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

Similar to the Doccano format, results for entities contain the text, start and stop character and the label. Using the visualization capabilities gives a similar picture to the Doccano tagging. As visible, the accuracy is pretty low. Similar excercises for english texts give much better results, since there are models available trained on much larger corpora.

displacy.render(doc, style="ent")